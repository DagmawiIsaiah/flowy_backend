"""This contains the developer end points."""

from fastapi import Depends, HTTPException, Response, status, APIRouter
from fastapi.params import Body
from sqlalchemy.orm import Session
from typing import List

from .. import models, schemas
from ..database import get_db


router = APIRouter(prefix="/v1/payments", tags=["payments"])


@router.post("/initiate")
def make_payment(payment: schemas.Payment, db: Session = Depends(get_db)):
    new_payment = models.Payment(**payment.model_dump())
    db.add(new_payment)
    db.commit()
    db.refresh(new_payment)
    return {"payment": new_payment}


@router.get("/{payer_id}", response_model=List[schemas.Payment])
async def get_payments_by_payer_id(payer_id: int, db: Session = Depends(get_db)):
    payments = db.query(models.Payment).filter(models.Payment.payer_id == payer_id).all()
    return payments


@router.get("/verify/{tx_ref}")
async def verify_payment(tx_ref: str, db: Session = Depends(get_db)):
    payment = db.query(models.Payment).filter(models.Payment.tx_ref == tx_ref).first()
    if payment:
        return {"payment": payment, "status": payment.status}
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"Error": f"No payment found by tx_ref {tx_ref}"})


@router.put("/status_update/{tx_ref}")
def update_payment(tx_ref: str, db: Session = Depends(get_db)):
    payment_query = db.query(models.Payment).filter(models.Payment.tx_ref == tx_ref)
    payment = payment_query.first()
    if payment:
        payment_query.update({"status": True}, synchronize_session=False)
        db.commit()
        return {"status": "sucessful"}
    
    
