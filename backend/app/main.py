from fastapi import FastAPI
from .database import engine, Base
from . import models
from .routes import router

app = FastAPI(title="PriceTrap Detector API")

Base.metadata.create_all(bind=engine)  # 👈 FIXED

app.include_router(router)

@app.get("/")
def root():
    return {"message": "PriceTrap backend is running 🚀"}
