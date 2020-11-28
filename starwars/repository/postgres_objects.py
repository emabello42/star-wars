from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Starship(Base):
    __tablename__ = "starships"
    id = Column(Integer, primary_key=True)
    code = Column(String(36), nullable=False)
    name = Column(String)
    hyperdrive_rating = Column(Float)