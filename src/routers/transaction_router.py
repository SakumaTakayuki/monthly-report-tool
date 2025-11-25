from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import SessionLocal
from db.models import Transaction
from schemas.transaction import (
    TransactionCreate,
    TransactionUpdate,
    TransactionResponse,
)

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/transactions", response_model=list[TransactionResponse])
def get_transactions(db: Session = Depends(get_db)):
    return db.query(Transaction).all()


@router.get("/transactions/{id}", response_model=TransactionResponse)
def get_transaction(id: int, db: Session = Depends(get_db)):
    data = db.query(Transaction).get(id)
    if not data:
        raise HTTPException(status_code=404, detail="Not found")
    return data


@router.post("/transactions", response_model=TransactionResponse)
def create_transaction(payload: TransactionCreate, db: Session = Depends(get_db)):
    new = Transaction(**payload.dict())
    db.add(new)
    db.commit()
    db.refresh(new)
    return new


@router.put("/transactions/{id}", response_model=TransactionResponse)
def update_transaction(
    id: int, payload: TransactionUpdate, db: Session = Depends(get_db)
):
    record = db.query(Transaction).get(id)
    if not record:
        raise HTTPException(status_code=404, detail="Not found")

    for key, value in payload.dict().items():
        setattr(record, key, value)

    db.commit()
    db.refresh(record)
    return record


@router.delete("/transactions/{id}")
def delete_transaction(id: int, db: Session = Depends(get_db)):
    record = db.query(Transaction).get(id)
    if not record:
        raise HTTPException(status_code=404, detail="Not found")

    db.delete(record)
    db.commit()
    return {"status": "deleted"}
