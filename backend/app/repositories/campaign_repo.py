from typing import Optional, List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models.campaign import Campaign

class CampaignRepository:

    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def get_campaign_by_id(self, campaign_id: int) -> Optional[Campaign]:
        q = select(Campaign).where(Campaign.id == campaign_id)
        result = await self.db_session.execute(q)
        return result.scalars().first()

    async def list_campaigns(self, limit: int = 50, offset: int = 0) -> List[Campaign]:
        q = select(Campaign).offset(offset).limit(limit)
        result = await self.db_session.execute(q)
        return result.scalars().all()

    async def add_campaign(self, campaign: Campaign) -> Campaign:
        try:
            self.db_session.add(campaign)
            await self.db_session.commit()
            await self.db_session.refresh(campaign)
            return campaign
        except Exception:
            await self.db_session.rollback()
            raise

    async def update_campaign(self, campaign: Campaign) -> Campaign:
        try:
            result = self.db_session.merge(campaign)
            await self.db_session.commit()
            await self.db_session.refresh(result)
            return result
        except Exception:
            await self.db_session.rollback()
            raise

    async def delete_campaign(self, campaign: Campaign) -> bool:
        try:
            self.db_session.delete(campaign)
            await self.db_session.commit()
            return True
        except Exception:
            await self.db_session.rollback()
            raise


