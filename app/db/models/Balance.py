from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Float
from sqlalchemy.orm import relationship

from app.db.base import Base


class Balance(Base):
    __tablename__ = "balances"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    datetime = Column(Date, index=True)
    balance = Column(Float, index=True)
    group_id = Column(Integer, ForeignKey("user_groups.id"))
    group = relationship("UserGroups", back_populates="balances")
