from sqlalchemy import Boolean, Column, ForeignKey, Integer, String ,Date
from sqlalchemy.orm import relationship

from app.db.base import Base


class Expense(Base):
    __tablename__ = "expenses"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    amount = Column(Integer, index=True)
    date = Column(Date, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="expenses")
    group_id = Column(Integer, ForeignKey("user_groups.id"))
    group = relationship("UserGroups", back_populates="expenses")