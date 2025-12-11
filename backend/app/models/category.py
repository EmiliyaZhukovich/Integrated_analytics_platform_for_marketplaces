from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database.database import Base

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key = True, index=True)
    name = Column(String, unique=True, nullable = False, index = True)
    slug = Column(String, unique=True, nullable = False, index = True)
    created_at = Column(DateTime, default = datetime.now, nullable=False)
    updated_at = Column(DateTime, default = datetime.now, onupdate=datetime.now, nullable=False)


    products = relationship('Product', back_populates='category_obj')

    def __repr__(self):
        return f"<Category(id={self.id}, name='{self.name}')>"
