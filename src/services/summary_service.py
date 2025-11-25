from sqlalchemy.orm import Session
from db.models import Transaction
from sqlalchemy import extract, func

def monthly_summary(db: Session, year: int):
    results = (
        db.query(
            extract("month", Transaction.date).label("month"),
            func.sum(Transaction.amount)
        )
        .filter(extract("year", Transaction.date) == year)
        .group_by("month")
        .all()
    )

    return {f"{year}-{int(month):02d}": total for month, total in results}

def category_summary(db: Session, start, end):
    results = (
        db.query(Transaction.category, func.sum(Transaction.amount))
        .filter(Transaction.date >= start, Transaction.date <= end)
        .group_by(Transaction.category)
        .all()
    )

    return {category: total for category, total in results}