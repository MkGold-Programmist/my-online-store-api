from pydantic import BaseModel
from datetime import datetime
from app.schemas.product import ProductResponse

class WishlistItemCreate(BaseModel):
    product_id: int

class WishlistItemResponse(BaseModel):
    id: int
    user_id: int
    product_id: int
    added_at: datetime
    product: ProductResponse

    class Config:
        from_attributes = True
