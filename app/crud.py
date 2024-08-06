# app/crud.py
from sqlalchemy.orm import Session
from . import models, schemas
from .auth import get_password_hash, verify_password


def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = models.User(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_test(db: Session, test: schemas.TestCreate):
    db_test = models.Test(**test.dict())
    db.add(db_test)
    db.commit()
    db.refresh(db_test)
    return db_test


def create_question(db: Session, question: schemas.QuestionCreate):
    db_question = models.Question(**question.dict())
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question


def create_answer(db: Session, answer: schemas.AnswerCreate):
    db_answer = models.Answer(**answer.dict())
    db.add(db_answer)
    db.commit()
    db.refresh(db_answer)
    return db_answer


# def get_test_results(db: Session, test_id: int):
#     # This is just an example. Adjust the query and returned data as needed.
#     results = db.query(models.Result).filter(models.Result.test_id == test_id).first()
#     if results:
#         return schemas.TestResults(
#             test_id=results.test_id,
#             user_id=results.user_id,
#             score=results.score,
#             total_questions=results.total_questions,
#             correct_answers=results.correct_answers,
#         )
#     return None
def get_test_results(db: Session, test_id: int):
    return db.query(models.Result).filter(models.Result.test_id == test_id).first()


def authenticate_user(db: Session, username: str, password: str):
    user = get_user_by_username(db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user


def create_test_result(db: Session, result: schemas.TestResultsCreate):
    db_result = models.Result(
        test_id=result.test_id,
        user_id=result.user_id,
        score=result.score,
        total_questions=result.total_questions,
        correct_answers=result.correct_answers,
    )
    db.add(db_result)
    db.commit()
    db.refresh(db_result)
    return db_result
