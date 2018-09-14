from sqlalchemy import Column, String, Text, BigInteger
from sqlalchemy.exc import OperationalError
from sqlalchemy.ext.declarative import declarative_base

from manager.manager_database import DatabaseManager

DBManager = DatabaseManager()
Base = declarative_base()
Base.metadata.bind = DBManager.fetch_engine()
try:
    Base.metadata.create_all()
except OperationalError:
    print("Unable to connect to database. Please check database settings in settings.py")
    exit()


class User(Base):
    __tablename__ = "user"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(Text, nullable=False)
