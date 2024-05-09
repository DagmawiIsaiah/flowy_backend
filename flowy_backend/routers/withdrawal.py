from typing import List
from fastapi import Depends, HTTPException, Response, status, APIRouter
from sqlalchemy.orm import Session

from .. import models, schemas
from ..database import get_db


router = APIRouter(prefix="/withdrawal", tags=["Withdrawal"])


@router.post("/create")
def create_withdrawal(withdrawal: schemas.Withdrawal, db: Session = Depends(get_db)):
    # TODO
    new_withdrawal = models.Withdrawal(**withdrawal.model_dump())
    db.add(new_withdrawal)
    db.commit()
    db.refresh(new_withdrawal)
    return new_withdrawal


@router.get("/")
def get_withdrawal_by_id(db: Session = Depends(get_db)):
    id = 1 # TODO
    withdrawals = db.query(models.Withdrawal).filter(models.Withdrawal.user_id == id).all()
    return withdrawals

