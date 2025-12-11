from sqlalchemy import Integer, String, Column, Float, ForeignKey, DateTime
from datetime import datetime
from sqlalchemy.orm import relationship

from app.database.database import Base

class Product(Base):
    __tablename__="products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id', ondelete="CASCADE"), nullable=False)
    price = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)
    created_at = Column(DateTime, default = datetime.now, nullable=False)
    updated_at = Column(DateTime, default = datetime.now, onupdate=datetime.now, nullable=False)

    category_obj = relationship('Category', back_populates='products')
    orders = relationship('Order', back_populates='product')
    campaigns = relationship('Campaign', back_populates='product')

    def __repr__(self):
        return f"<Product(id={self.id}, name={self.name}, category={self.category_obj}, price={self.price}, stock={self.stock})>"
