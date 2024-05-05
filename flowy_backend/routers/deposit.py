from fastapi import Depends, HTTPException, Response, status, APIRouter
from sqlalchemy.orm import Session

from .. import models, schemas
# from ..database import SessionLocal, get_db


router = APIRouter(prefix="/deposit", tags=["Deposit"])


@router.post("/create")
def create_deposit(user: schemas.Deposit):
    return {"status": "200"}


@router.get("/{id}")
def get_deposit_by_id(id: int):
    pass

