"""This contains the developer end points."""

from typing import List
from fastapi import Depends, HTTPException, Response, status, APIRouter
from sqlalchemy.orm import Session

from .. import models, schemas
# from ..database import SessionLocal, get_db


router = APIRouter(prefix="/transfer", tags=["Transfer"])


@router.post("/transfer")
def transfer(user: str, payload: schemas.Transfer):
    return {"status": "200"}


@router.get("/transfer")
def get_transfer_by_id(user: str, tx_ref: dict):
    return {"status": "200"}

