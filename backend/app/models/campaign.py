from sqlalchemy import Integer, String, Column, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database.database import Base

class Campaign(Base):
    __tablename__="campaigns"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey('products.id', ondelete="CASCADE"), nullable=False)
    platform = Column(String, nullable=False)  # Wildberries, Ozon, Yandex.Market
    budget = Column(Float, nullable=False)
    impressions = Column(Integer, nullable=True)
    clicks = Column(Integer, nullable=True)
    conversions = Column(Integer, nullable=True)
    created_at = Column(DateTime, default = datetime.now, nullable=False)
    updated_at = Column(DateTime, default = datetime.now, onupdate=datetime.now, nullable=False)

    product = relationship("Product", back_populates="campaigns")

    def __repr__(self):
        return f"<Campaign(id={self.id}, product_id={self.product_id}, budget={self.budget})>"
