from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class CampaignBase(BaseModel):
    product_id: int = Field(..., description='ID of the product associated with the campaign')
    platform: str = Field(..., min_length=3, max_length=100, description='Platform where the campaign is run (e.g., Wildberries, Ozon, Yandex.Market)')
    budget: float = Field(..., gt=0, description='Budget allocated for the campaign')
    impressions: Optional[int] = Field(None, ge=0, description='Number of impressions for the campaign')
    clicks: Optional[int] = Field(None, ge=0, description='Number of clicks for the campaign')
    conversions: Optional[int] = Field(None, ge=0, description='Number of conversions for the campaign')

class CampaignCreate(CampaignBase):
    pass

class CampaignUpdate(BaseModel):
    product_id: Optional[int] = Field(None, description='ID of the product associated with the campaign')
    platform: Optional[str] = Field(None, min_length=3, max_length=100, description='Platform where the campaign is run')
    budget: Optional[float] = Field(None, gt=0, description='Budget allocated for the campaign')
    impressions: Optional[int] = Field(None, ge=0, description='Number of impressions')
    clicks: Optional[int] = Field(None, ge=0, description='Number of clicks')
    conversions: Optional[int] = Field(None, ge=0, description='Number of conversions')

class CampaignResponse(CampaignBase):
    id: int = Field(..., description='Unique identifier of the campaign')
    created_at: datetime = Field(..., description='Timestamp when campaign was created')
    updated_at: datetime = Field(..., description='Timestamp when campaign was last updated')

    class Config:
        from_attributes = True
