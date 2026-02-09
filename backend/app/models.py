from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from datetime import datetime
from .database import Base   # 👈 THIS LINE IS CRITICAL


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    product_id = Column(String, unique=True, index=True)
    name = Column(String)
    platform = Column(String)


class PriceHistory(Base):
    __tablename__ = "price_history"

    id = Column(Integer, primary_key=True)
    product_id = Column(String, ForeignKey("products.product_id"))
    price = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)
