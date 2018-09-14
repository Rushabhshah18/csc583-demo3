from sqlalchemy import Column, String, Text, BigInteger
from sqlalchemy.ext.declarative import declarative_base

from manager.manager_database import DatabaseManager

DBManager = DatabaseManager()
Base = declarative_base()
Base.metadata.bind = DBManager.fetch_engine()
Base.metadata.create_all(DBManager.fetch_engine())


class User(Base):
    __tablename__ = "user"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(Text, nullable=False)
