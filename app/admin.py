from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from . import auth, database, models
from . import schemas

router = APIRouter()


@router.post("/tests/", response_model=schemas.Test)
def create_test(
    test: schemas.TestCreate,
    db: Session = Depends(database.SessionLocal),
    current_user: schemas.User = Depends(auth.get_current_user),
):
    if not current_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Not enough permissions"
        )
    db_test = models.Test(**test.dict())
    db.add(db_test)
    db.commit()
    db.refresh(db_test)
    return db_test
