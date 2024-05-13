from fastapi import Depends, HTTPException, Response, status, APIRouter
from sqlalchemy.orm import Session

from .. import models, schemas, oauth2
from ..database import get_db


router = APIRouter(prefix="/project", tags=["Project"])


@router.post("/create")
def create_project(project: schemas.Project, db: Session = Depends(get_db), user_id: int = Depends(oauth2.get_current_user)):
    new_project = models.Project(**project.model_dump())
    new_project.user_id = user_id.id
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return new_project


@router.get("/{id}")
def get_project_by_id(id: int, db: Session = Depends(get_db), user_id: int = Depends(oauth2.get_current_user)):
    project = db.query(models.Project).filter(
        models.Project.user_id == user_id.id, models.Project.id == id).first()
    return project


@router.put("/udpate_api/id")
def update_project_api_key(id: int, db: Session = Depends(get_db), user_id: int = Depends(oauth2.get_current_user)):
    project_query = db.query(models.Project).filter(
        models.Project.user_id == user_id.id, models.Project.id == id)
    project = project_query.first()
    if project:
        new_api_key = ""  # auto generate api key
        project_query.update({"api_key": new_api_key},
                             synchronize_session=False)
        db.commit()


@router.put("/update_status/id")
def update_project_status(id: int, db: Session = Depends(get_db), user_id: int = Depends(oauth2.get_current_user)):
    project_query = db.query(models.Project).filter(
        models.Project.user_id == user_id.id, models.Project.id == id)
    project = project_query.first()
    if project:
        status = not project.status
        project_query.update({"status": status},
                             synchronize_session=False)
        db.commit()


@router.delete("/{id}")
def delete_project(id: int):
    return {"status": "200"}
