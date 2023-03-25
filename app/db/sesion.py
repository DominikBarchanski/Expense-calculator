from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

engine = create_engine(settings.SQLALCHEMY_DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def create_database_tables():
    from app.db.base import Base
    from app.db.models.UserGroupMembership import UserGroupMembership
    from app.db.models.User import User
    from app.db.models.UsersGroups import UserGroups
    from app.db.models.Expenses import Expense
    from app.db.models.Balance import Balance
    Base.metadata.create_all(bind=engine)
