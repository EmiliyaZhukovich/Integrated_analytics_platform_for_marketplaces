from typing import Optional, List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models.category import Category

class CategoryRepository:

    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def get_category_by_id(self, category_id: int) -> Optional[Category]:
        q = select(Category).where(Category.id == category_id)
        result = await self.db_session.execute(q)
        return result.scalars().first()

    async def get_category_by_name(self, name:str) -> Optional[Category]:
        q = select(Category).where(Category.name == name)
        result = await self.db_session.execute(q)
        return result.scalars().first()

    async def list_categories(self, limit: int = 50, offset: int = 0) -> List[Category]:
        q = select(Category).offset(offset).limit(limit)
        result = await self.db_session.execute(q)
        return result.scalars().all()

    async def add_category(self, category: Category) -> Category:
        try:
            self.db_session.add(category)
            await self.db_session.commit()
            await self.db_session.refresh(category)
            return category
        except Exception:
            await self.db_session.rollback()
            raise
    async def update_category(self, category: Category) -> Category:
        try:
            result = self.db_session.merge(category)
            await self.db_session.commit()
            await self.db_session.refresh(result)
            return result
        except Exception:
            await self.db_session.rollback()
            raise

    async def delete_category(self, category: Category) -> bool:
        try:
            self.db_session.delete(category)
            await self.db_session.commit()
            return True
        except Exception:
            await self.db_session.rollback()
            raise

