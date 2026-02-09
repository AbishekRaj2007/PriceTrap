from pydantic import BaseModel
from datetime import datetime
class PriceTrackRequest(BaseModel):
    product_id: str
    name: str
    price: float
    platform: str

class PriceHistoryResponse(BaseModel):
    price: float
    timestamp: datetime