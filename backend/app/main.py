from fastapi import FastAPI
from .database import engine, Base
from . import models
from .routes import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="PriceTrap Detector API")

Base.metadata.create_all(bind=engine)  # 👈 FIXED

app.include_router(router)

@app.get("/")
def root():
    return {"message": "PriceTrap backend is running 🚀"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)