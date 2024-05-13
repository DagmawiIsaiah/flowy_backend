from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from .. import models, schemas
from ..database import get_db
from .. import oauth2


router = APIRouter(prefix="/deposit", tags=["Deposit"])


@router.post("/create")
def create_deposit(deposit: schemas.Deposit, db: Session = Depends(get_db), user_id: int = Depends(oauth2.get_current_user)):
    new_deposit = models.Deposit(**deposit.model_dump())
    new_deposit.user_id = user_id.id
    db.add(new_deposit)
    db.commit()
    db.refresh(new_deposit)
    return new_deposit


@router.get("/")
def get_deposits(db: Session = Depends(get_db), user_id: int = Depends(oauth2.get_current_user)):
    deposits = db.query(models.Deposit).filter(
        models.Deposit.user_id == user_id.id).all()
    return deposits

