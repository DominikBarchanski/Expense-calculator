from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.sesion import SessionLocal
from app.db.models.ProductCategory import ProductCategory

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/category", status_code=200)
def get_category(db: Session = Depends(get_db)):
    category = db.query(ProductCategory).all()
    return category
