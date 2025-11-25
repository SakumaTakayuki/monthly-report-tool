from fastapi import FastAPI
from routers.csv_router import router as csv_router
from routers.transaction_router import router as transaction_router
from routers.summary_router import router as summary_router

app = FastAPI(title="CSV Import & Transaction API")
app.include_router(csv_router, prefix="/api")
app.include_router(transaction_router, prefix="/api")
app.include_router(summary_router, prefix="/api")

@app.get("/health")
def health_check():
    return {"status": "ok"}