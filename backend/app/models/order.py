from sqlalchemy import Integer, String, Column, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from app.database.database import Base


class Order(Base):
    __tablename__="orders"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey('products.id', ondelete="CASCADE"), nullable=False)
    quantity = Column(Integer, nullable=False)
    total_price = Column(Float, nullable=False)
    order_date = Column(DateTime, nullable=False)
    marketplace = Column(String, nullable=False)  # Wildberries, Ozon, Yandex.Market
    created_at = Column(DateTime, default = datetime.now, nullable=False)
    updated_at = Column(DateTime, default = datetime.now, onupdate=datetime.now, nullable=False)


    product = relationship("Product", back_populates="orders")


    def __repr__(self):
        return f"<Order(id={self.id}, product_id={self.product_id}, quantity={self.quantity}, total_price={self.total_price}, order_date={self.order_date})>"
