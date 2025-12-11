from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

from .category import CategoryResponse

class ProductBase(BaseModel):
    name: str = Field(..., min_length=5, max_length=200, description='Product name')
    category_id: int = Field(..., description='ID of the category the product belongs to')
    price: float = Field(..., gt=0, description='Price of the product')
    stock: int = Field(..., ge=0, description='Available stock of the product')

class ProductCreate(ProductBase):
    pass

class ProductUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=5, max_length=200, description='Product name')
    category_id: Optional[int] = Field(None, description='ID of the category')
    price: Optional[float] = Field(None, gt=0, description='Price of the product')
    stock: Optional[int] = Field(None, ge=0, description='Available stock')

class ProductResponse(ProductBase):
    id: int = Field(..., description='Unique identifier of the product')
    category: CategoryResponse = Field(..., description='Category information')
    created_at: datetime = Field(..., description='Timestamp when product was created')
    updated_at: datetime = Field(..., description='Timestamp when product was last updated')

    class Config:
        from_attributes = True
