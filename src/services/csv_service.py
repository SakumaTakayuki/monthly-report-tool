import pandas as pd
from sqlalchemy.orm import Session
from utils.cleaner import clean_csv
from db.models import Transaction

def import_csv_to_db(file, db: Session):
    df = pd.read_csv(file)
    df = clean_csv(df)

    records = []
    for _, row in df.iterrows():
        record = Transaction(
            date=row["date"],
            category=row["category"],
            description=row.get("description", ""),
            amount=row["amount"]
        )
        records.append(record)

    db.bulk_save_objects(records)
    db.commit()

    return len(records)