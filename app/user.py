from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from . import auth, database, models
from . import schemas

router = APIRouter()


@router.get("/tests/", response_model=List[schemas.Test])
def read_tests(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(database.SessionLocal),
    current_user: schemas.User = Depends(auth.get_current_user),
):
    tests = db.query(models.Test).offset(skip).limit(limit).all()
    return tests


@router.post("/submissions/", response_model=schemas.Submission)
def submit_answers(
    submission: schemas.SubmissionCreate,
    db: Session = Depends(database.SessionLocal),
    current_user: schemas.User = Depends(auth.get_current_user),
):
    db_submission = models.Submission(**submission.dict(), user_id=current_user.id)
    db.add(db_submission)
    db.commit()
    db.refresh(db_submission)
    return db_submission
