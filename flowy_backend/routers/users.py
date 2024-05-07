from fastapi import Depends, HTTPException, Response, status, APIRouter
from sqlalchemy.orm import Session

from .. import models, schemas
from ..database import get_db
from .. import utils

router = APIRouter(prefix="/user", tags=["User"])


@router.post("/create", response_model=schemas.UserResponse)
def create_user(user: schemas.User, db: Session = Depends(get_db)):
    hash_password = utils.hash(user.password)
    user.password = hash_password
    user.balance = 0.0
    user.flowy_account_number = int(user.phone_number)
    # create account number
    new_user = models.User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/{id}", response_model=schemas.UserResponse)
def get_user_by_id(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    return user


@router.put("/id")
def update_user(id: int, db: Session = Depends(get_db)):
    pass

@router.delete("/{id}")
def delete_user(id: int, db: Session = Depends(get_db)):
    return {"status": "200"}

