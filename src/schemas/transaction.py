from pydantic import BaseModel
from datetime import date

class TransactionBase(BaseModel):
    date: date
    category: str
    description: str | None = None
    amount: int

class TransactionCreate(TransactionBase):
    pass

class TransactionUpdate(TransactionBase):
    pass

class TransactionResponse(TransactionBase):
    id: int

    class Config:
        orm_mode = True