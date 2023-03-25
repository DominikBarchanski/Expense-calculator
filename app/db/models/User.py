from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base import Base



class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)
    hashed_password = Column(String)
    memberships = relationship("UserGroupMembership", back_populates="user")
    expenses = relationship("Expense", back_populates="user")
    balances = relationship("Balance", back_populates="user")
