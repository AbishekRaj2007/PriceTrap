from pydantic import BaseModel

class PriceTrackRequest(BaseModel):
    product_id: str
    name: str
    price: float
    platform: str