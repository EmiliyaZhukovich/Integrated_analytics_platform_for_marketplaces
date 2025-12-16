from typing import Optional, List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models.order import Order

class OrderRepository:

    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def get_order_by_id(self, order_id: int) -> Optional[Order]:
        q = select(Order).where(Order.id == order_id)
        result = await self.db_session.execute(q)
        return result.scalars().first()

    async def list_orders(self, limit: int = 50, offset: int = 0) -> List[Order]:
        q = select(Order).offset(offset).limit(limit)
        result = await self.db_session.execute(q)
        return result.scalars().all()

    async def add_order(self, order: Order) -> Order:
        try:
            self.db_session.add(order)
            await self.db_session.commit()
            await self.db_session.refresh(order)
            return order
        except Exception:
            await self.db_session.rollback()
            raise

    async def update_order(self, order: Order) -> Order:
        try:
            result = self.db_session.merge(order)
            await self.db_session.commit()
            await self.db_session.refresh(result)
            return result
        except Exception:
            await self.db_session.rollback()
            raise

    async def delete_order(self, order: Order) -> bool:
        try:
            self.db_session.delete(order)
            await self.db_session.commit()
            return True
        except Exception:
            await self.db_session.rollback()
            raise
