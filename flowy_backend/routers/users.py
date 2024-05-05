from typing import List
from fastapi import Depends, HTTPException, Response, status, APIRouter
from sqlalchemy.orm import Session

from .. import models, schemas
# from ..database import SessionLocal, get_db


router = APIRouter(prefix="/user", tags=["User"])


@router.post("/create")
def create_user(user: schemas.User):
    return {"status": "200"}


@router.get("/{id}")
def get_user_by_id(id: int):
    pass


@router.put("/id")
def update_user(id: int):
    pass

@router.delete("/{id}")
def delete_user(id: int):
    return {"status": "200"}

