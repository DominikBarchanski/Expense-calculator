from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.sesion import SessionLocal
from app.db.models.Balance import Balance
from app.db.schemas.Balance import BalanceCreate

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/add_balance", status_code=201)
def add_balance(balance: BalanceCreate, db: Session = Depends(get_db)):
    db_balance = Balance(group_id=balance.group_id, balance=balance.balance, datetime=balance.datetime)
    db.add(db_balance)
    db.commit()
    db.refresh(db_balance)
    return db_balance

@router.get("/get_balance/{group_id}", status_code=200)
def get_balance(group_id: int, db: Session = Depends(get_db)):
    balance = db.query(Balance).filter(Balance.group_id == group_id).all()
    return balance


