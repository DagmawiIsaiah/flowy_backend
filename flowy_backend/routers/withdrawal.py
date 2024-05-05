from typing import List
from fastapi import Depends, HTTPException, Response, status, APIRouter
from sqlalchemy.orm import Session

from .. import models, schemas
# from ..database import SessionLocal, get_db


router = APIRouter(prefix="/withdrawal", tags=["Withdrawal"])


@router.post("/create")
def create_withdrawal(user: schemas.Withdrawal):
    return {"status": "200"}


@router.get("/{id}")
def get_withdrawal_by_id(id: int):
    pass

