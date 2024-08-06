# app/main.py
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import engine, SessionLocal
from .auth import get_password_hash, create_access_token, get_current_user
from fastapi.security import OAuth2PasswordRequestForm


app = FastAPI()

models.Base.metadata.create_all(bind=engine)
import logging

logger = logging.getLogger(__name__)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return crud.create_user(db=db, user=user)


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        logger.error(f"User with username {user.username} already registered")
        raise HTTPException(status_code=400, detail="Username already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/{username}", response_model=schemas.User)
def get_user(username: str, db: Session = Depends(get_db)):
    user = crud.get_user_by_username(db, username=username)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.post("/token", response_model=schemas.Token)
def login_for_access_token(
    db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()
):
    user = crud.authenticate_user(
        db, username=form_data.username, password=form_data.password
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}


@app.post("/tests/", response_model=schemas.Test)
def create_test(test: schemas.TestCreate, db: Session = Depends(get_db)):
    return crud.create_test(db=db, test=test)


@app.get("/tests/{test_id}/results/", response_model=schemas.TestResults)
def get_test_results(test_id: int, db: Session = Depends(get_db)):
    results = crud.get_test_results(db=db, test_id=test_id)
    if not results:
        raise HTTPException(status_code=404, detail="Test results not found")
    return results


@app.post("/questions/", response_model=schemas.Question)
def create_question(question: schemas.QuestionCreate, db: Session = Depends(get_db)):
    return crud.create_question(db=db, question=question)


@app.post("/answers/", response_model=schemas.Answer)
def create_answer(answer: schemas.AnswerCreate, db: Session = Depends(get_db)):
    return crud.create_answer(db=db, answer=answer)


@app.get("/tests/{test_id}/results/", response_model=schemas.TestResults)
def get_test_results(test_id: int, db: Session = Depends(get_db)):
    results = crud.get_test_results(db=db, test_id=test_id)
    if not results:
        logger.error(f"Test results for test_id {test_id} not found")
        raise HTTPException(status_code=404, detail="Test results not found")
    return results


@app.post("/results/", response_model=schemas.TestResults)
def create_test_result(
    result: schemas.TestResultsCreate, db: Session = Depends(get_db)
):
    return crud.create_test_result(db=db, result=result)


# Additional endpoints for CRUD operations
