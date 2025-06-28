# app/services/product_service.py

from typing import List
from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.product import Product
from app.schemas.product import ProductCreate, ProductUpdate

class ProductService:
    @staticmethod
    async def create(db: AsyncSession, data: ProductCreate) -> Product:
        obj = Product(**data.dict())
        db.add(obj)
        await db.commit()
        await db.refresh(obj)
        return obj

    @staticmethod
    async def get_all(db: AsyncSession, skip: int = 0, limit: int = 100) -> List[Product]:
        result = await db.execute(select(Product).offset(skip).limit(limit))
        return result.scalars().all()

    @staticmethod
    async def get(db: AsyncSession, product_id: int) -> Product | None:
        return await db.get(Product, product_id)

    @staticmethod
    async def update(db: AsyncSession, product_id: int, data: ProductUpdate) -> Product | None:
        update_data = {k: v for k, v in data.dict().items() if v is not None}
        if update_data:
            await db.execute(
                update(Product)
                .where(Product.id == product_id)
                .values(**update_data)
            )
            await db.commit()
        return await db.get(Product, product_id)

    @staticmethod
    async def delete(db: AsyncSession, product_id: int) -> None:
        await db.execute(delete(Product).where(Product.id == product_id))
        await db.commit()
