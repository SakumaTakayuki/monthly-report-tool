from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db.database import SessionLocal
from services.summary_service import monthly_summary, category_summary

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/summary/monthly")
def summary_monthly(year: int, db: Session = Depends(get_db)):
    return monthly_summary(db, year)


@router.get("/summary/category")
def summary_by_category(start: str, end: str, db: Session = Depends(get_db)):
    return category_summary(db, start, end)
