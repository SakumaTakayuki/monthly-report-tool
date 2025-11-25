from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session
from db.database import SessionLocal
from services.csv_service import import_csv_to_db

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/upload-csv")
async def upload_csv(file: UploadFile = File(...), db: Session = Depends(get_db)):
    inserted = import_csv_to_db(file.file, db)
    return {"status": "success", "inserted": inserted}
