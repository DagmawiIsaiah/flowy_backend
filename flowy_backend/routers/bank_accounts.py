from fastapi import Depends, HTTPException, Response, status, APIRouter
from sqlalchemy.orm import Session

from .. import models, schemas
# from ..database import SessionLocal, get_db


router = APIRouter(prefix="/accounts", tags=["BankAccounts"])


@router.post("/create")
def create_account(user: schemas.UserBankAccounts):
    return {"status": "200"}


@router.get("/{id}")
def get_account_by_id(id: int):
    pass


@router.put("/id")
def update_account(id: int):
    pass

@router.delete("/{id}")
def delete_account(id: int):
    return {"status": "200"}

