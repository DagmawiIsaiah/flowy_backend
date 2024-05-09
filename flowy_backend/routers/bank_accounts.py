from fastapi import Depends, HTTPException, Response, status, APIRouter
from sqlalchemy.orm import Session

from .. import models, schemas
from ..database import get_db


router = APIRouter(prefix="/accounts", tags=["BankAccounts"])


@router.post("/create")
def create_account(account: schemas.BankAccounts, db: Session = Depends(get_db)):
    new_account = models.Accounts(**account.model_dump())
    db.add(new_account)
    db.commit()
    db.refresh(new_account)
    return new_account


@router.get("/")
def get_account(db: Session = Depends(get_db)):
    id = 1 # TODO: This part is suppose to be changed when auth is implemented.
    accounts = db.query(models.Accounts).filter(models.Accounts.user_id == id).all()
    return accounts


@router.put("/id")
def update_account(id: int, db: Session = Depends(get_db)):
    user_id = 1 # TODO
    account_query = db.query(models.BankAccounts).filter(models.BankAccounts.id == id, models.BankAccounts.user_id == user_id)
    account = account_query.first()
    if account:
        account_query.update({"bank_id": update_account.name, "account_number": update_account.account_number}, synchronize_session=False)
        db.commit()
        return {"status": "sucessful"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"Account not found"})
    

@router.delete("/{id}")
def delete_account(id: int, db: Session = Depends(get_db)):
    user_id = 1 # TODO: changed when auth is implemented
    account = db.query(models.BankAccounts).filter(models.BankAccounts.id == id, models.BankAccounts.user_id == user_id)
    if account.first():
        account.delete(synchronize_session=False)
        db.commit()
        return {"cmd": "account deletion complete"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"Account not found"})
