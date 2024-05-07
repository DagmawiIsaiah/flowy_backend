from fastapi import Depends, HTTPException, Response, status, APIRouter
from sqlalchemy.orm import Session
from passlib.context import CryptContext

from .. import models, schemas
from ..database import get_db
from .. import utils


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/login")
def login(credentials: schemas.Login, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.phone_number == credentials.phone_number).first()
    
    if user:
        utils.verify_pwd(credentials.password, user.password)
        return {"token": "example token"}
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"User not found"})


@router.get("/logout")
def logout(id: int, db: Session = Depends(get_db)):
    return {"status": "200"}

