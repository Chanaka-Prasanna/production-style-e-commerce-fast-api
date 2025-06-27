from sqlalchemy import Column, Integer, String, Numeric, DateTime, func
from app.db.base import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer,primary_key=True,index=True)
    name = Column(String(100),nullable=False)
    description = Column(String(500),nullable=False)
    price = Column(Numeric(10,2),nullable=False)
    in_stock = Column(Integer,default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())


