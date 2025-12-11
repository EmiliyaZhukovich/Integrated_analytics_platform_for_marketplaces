from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class CategoryBase(BaseModel):
    name: str = Field(..., min_length=3, max_length=100, description='Category name')
    slug: str = Field(..., min_length=3, max_length=100, description='URL-friendly category identifier')

class CategoryCreate(CategoryBase):
    pass

class CategoryUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=3, max_length=100, description='Category name')
    slug: Optional[str] = Field(None, min_length=3, max_length=100, description='URL-friendly category identifier')

class CategoryResponse(CategoryBase):
    id: int = Field(..., description='Unique identifier of the category')
    created_at: datetime = Field(..., description='Timestamp when category was created')
    updated_at: datetime = Field(..., description='Timestamp when category was last updated')

    class Config:
        from_attributes = True
