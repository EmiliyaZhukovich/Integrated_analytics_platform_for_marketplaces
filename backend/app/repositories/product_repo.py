from typing import Optional, List, Dict, Any
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select


from app.models.product import Product

class ProductRepository:

    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def get_product_by_id(self, product_id: int) -> Optional[Product]:
        q = select(Product).where(Product.id == product_id)
        result = await self.db_session.execute(q)
        return result.scalars().first()

    async def list_products(self, filters: Dict[str, Any] = None, limit: int = 50, offset: int = 0) -> List[Product]:
        q = self.db_session.query(Product)
        if filters:
            if 'category' in filters:
                q = q.filter(Product.category == filters['category'])
            if 'price_min' in filters:
                q = q.filter(Product.price >= filters['price_min'])
            if 'price_max' in filters:
                q = q.filter(Product.price <= filters['price_max'])
            if 'name' in filters:
                q = q.filter(Product.name.ilike(f"%{filters['name']}%"))
        q = q.offset(offset).limit(limit)
        result = await self.db_session.execute(q)
        return result.scalars().all()


    async def add_product(self, product: Product) -> Product:
        try:
            self.db_session.add(product)
            await self.db_session.commit()
            await self.db_session.refresh(product)
            return product
        except Exception:
            await self.db_session.rollback()
            raise

    async def update_product(self, product: Product) -> Product:
        try:
            result = self.db_session.merge(product)
            await self.db_session.commit()
            await self.db_session.refresh(result)
            return result
        except Exception:
            await self.db_session.rollback()
            raise

    async def delete_product(self, product: Product) -> bool:
        try:
            self.db_session.delete(product)
            await self.db_session.commit()
            return True
        except Exception:
            await self.db_session.rollback()
            raise

