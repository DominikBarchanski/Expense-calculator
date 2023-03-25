from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.db.base import Base



class UserGroups(Base):
    __tablename__ = "user_groups"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    members = relationship("UserGroupMembership", back_populates="group")
    expenses = relationship("Expense", back_populates="group")
    balances = relationship("Balance", back_populates="group")

