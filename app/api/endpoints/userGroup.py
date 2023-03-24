from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.sesion import SessionLocal
from app.db.models.UsersGroups import UserGroups
from app.db.schemas.UsersGroups import UsersGroupsCreate

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/create_group", status_code=201)
def create_group(group: UsersGroupsCreate, db: Session = Depends(get_db)):
    db_group = db.query(UserGroups).filter(UserGroups.name == group.name).first()
    if db_group:
        raise HTTPException(status_code=400, detail="Group already exists")
    db_group = UserGroups(name=group.name)
    db.add(db_group)
    db.commit()
    db.refresh(db_group)
    return db_group

@router.get("/get_groups", status_code=200)
def get_groups(db: Session = Depends(get_db)):
    groups = db.query(UserGroups).all()
    return groups
