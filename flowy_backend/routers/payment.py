"""This contains the developer end points."""

from fastapi import Depends, HTTPException, Response, status, APIRouter
from sqlalchemy.orm import Session

from .. import models, schemas
# from ..database import SessionLocal, get_db


router = APIRouter(prefix="/v1/payments", tags=["payments"])


@router.post("/recive")
def recive_payment(header: str, payload: schemas.Payment):
    return {"status": "200"}


@router.get("/verify")
def verify_payment(header: str, tx_ref: dict):
    return {"status": "200"}


@router.put("/update")
def update_payment(header: str, payload: dict):
    pass


@router.delete("/delete")
def delete_payment(header: str, id: int):
    pass
