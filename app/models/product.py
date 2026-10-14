from sqlalchemy import Column, Integer, String, Float, Boolean, Text
from app.database.database import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, nullable=False, index=True)
    description = Column(Text, nullable=True)
    category = Column(String, nullable=False, index=True)
    price = Column(Float, nullable=False)
    old_price = Column(Float, nullable=True)
    stock_quantity = Column(Integer, default=0)
    brand = Column(String, nullable=True)
    image_url = Column(String, nullable=True)
    is_new = Column(Boolean, default=False)
    is_on_sale = Column(Boolean, default=False)
    discount_percentage = Column(Integer, default=0)
    is_active = Column(Boolean, default=True)
