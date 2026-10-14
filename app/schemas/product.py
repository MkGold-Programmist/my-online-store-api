from pydantic import BaseModel

class ProductBase(BaseModel):
    title: str
    description: str | None = None
    category: str
    price: float
    old_price: float | None = None
    stock_quantity: int = 0
    brand: str | None = None
    image_url: str | None = None
    is_new: bool = False
    is_on_sale: bool = False
    discount_percentage: int = 0
    is_active: bool = True

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    category: str | None = None
    price: float | None = None
    old_price: float | None = None
    stock_quantity: int | None = None
    brand: str | None = None
    image_url: str | None = None
    is_new: bool | None = None
    is_on_sale: bool | None = None
    discount_percentage: int | None = None
    is_active: bool | None = None

class ProductResponse(ProductBase):
    id: int

    class Config:
        from_attributes = True
