from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class OrderBase(BaseModel):
    product_id: int = Field(..., description='ID of the product')
    quantity: int = Field(..., gt=0, description='Quantity of the product ordered')
    total_price: float = Field(..., gt=0, description='Total price of the order')
    order_date: datetime = Field(..., description='Date and time when the order was placed')
    marketplace: str = Field(..., min_length=3, max_length=100, description='Marketplace where the order was placed (e.g., Wildberries, Ozon, Yandex.Market)')

class OrderCreate(OrderBase):
    pass

class OrderUpdate(BaseModel):
    product_id: Optional[int] = Field(None, description='ID of the product')
    quantity: Optional[int] = Field(None, gt=0, description='Quantity of the product ordered')
    total_price: Optional[float] = Field(None, gt=0, description='Total price of the order')
    order_date: Optional[datetime] = Field(None, description='Date and time when the order was placed')
    marketplace: Optional[str] = Field(None, min_length=3, max_length=100, description='Marketplace where the order was placed')

class OrderResponse(OrderBase):
    id: int = Field(..., description='Unique identifier of the order')
    created_at: datetime = Field(..., description='Timestamp when order was created')
    updated_at: datetime = Field(..., description='Timestamp when order was last updated')

    class Config:
        from_attributes = True
