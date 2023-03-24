from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.db.base import Base


class UserGroupMembership(Base):
    __tablename__ = 'user_group_memberships'
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    group_id = Column(Integer, ForeignKey('user_groups.id'))
    user = relationship("User", back_populates="memberships")
    group = relationship("UserGroups", back_populates="members")
