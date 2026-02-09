from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .database import get_db
from . import models, schemas

router = APIRouter()

@router.post("/track-price")
def track_price(data: schemas.PriceTrackRequest, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(
        models.Product.product_id == data.product_id
    ).first()

    if not product:
        product = models.Product(
            product_id=data.product_id,
            name=data.name,
            platform=data.platform
        )
        db.add(product)
        db.commit()

    price_entry = models.PriceHistory(
        product_id=data.product_id,
        price=data.price
    )

    db.add(price_entry)
    db.commit()

    return {
        "message": "Price tracked successfully",
        "product_id": data.product_id,
        "price": data.price
    }
@router.get("/price-history/{product_id}")
def get_price_history(product_id: str, db: Session = Depends(get_db)):
    history = db.query(models.PriceHistory).filter(
        models.PriceHistory.product_id == product_id
    ).order_by(models.PriceHistory.timestamp.asc()).all()

    return [
        {
            "price": record.price,
            "timestamp": record.timestamp
        }
        for record in history
    ]