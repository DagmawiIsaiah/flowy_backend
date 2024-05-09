from fastapi import Depends, HTTPException, Response, status, APIRouter
from sqlalchemy.orm import Session

from .. import models, schemas
from ..database import get_db


router = APIRouter(prefix="/banks", tags=["Banks"])


@router.get("/")
def get_banks(db: Session = Depends(get_db)):
    bank = db.query(models.Bank).all()
    return bank
