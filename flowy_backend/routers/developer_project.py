from fastapi import Depends, HTTPException, Response, status, APIRouter
from sqlalchemy.orm import Session

from .. import models, schemas
from ..database import get_db


router = APIRouter(prefix="/project", tags=["Project"])


@router.post("/create")
def create_project(user: schemas.Project):
    return {"status": "200"}


@router.get("/{id}")
def get_project_by_id(id: int):
    pass


@router.put("/id")
def update_project(id: int):
    pass

@router.delete("/{id}")
def delete_project(id: int):
    return {"status": "200"}

