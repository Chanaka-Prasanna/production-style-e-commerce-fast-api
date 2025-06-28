# app/schemas/product.py

from pydantic import BaseModel, Field
from decimal import Decimal
from datetime import datetime

class ProductBase(BaseModel):
    name: str = Field(..., max_length=100)
    description: str | None = Field(None, max_length=500)
    price: Decimal
    in_stock: int = 0

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    name: str | None = Field(None, max_length=100)
    description: str | None = Field(None, max_length=500)
    price: Decimal | None = None
    in_stock: int | None = None

class ProductOut(ProductBase):
    id: int
    created_at: datetime
    updated_at: datetime | None

    class Config:
        orm_mode = True
