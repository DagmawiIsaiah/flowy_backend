from typing import List
from fastapi import Depends, HTTPException, Response, status, APIRouter
from sqlalchemy.orm import Session

from .. import models, schemas
from ..database import get_db


router = APIRouter(prefix="/transfer", tags=["Transfer"])


@router.post("/transfer")
def transfer(transfer: schemas.Transfer, db: Session = Depends(get_db)):
    # TODO
    new_transfer = models.Transfer(**transfer.model_dump())
    db.add(new_transfer)
    db.commit()
    db.refresh(new_transfer)
    return new_transfer


@router.get("/transfer")
def get_transfer(db: Session = Depends(get_db)):
    id = 1 # TODO
    transfers = db.query(models.Transfer).filter(models.Transfer.sender_id == id).all()
    return transfers

