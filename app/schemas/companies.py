from database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Companies(Base):
    __tablename__ = "companies"
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    name = Column(String, unique=True)
    password = Column(String)
    email = Column(String, nullable=True, unique=True)
    employees = relationship('Employees', back_populates='company', cascade="all, delete-orphan")
    cameras = relationship('Cameras', back_populates='company', cascade="all, delete-orphan")
    events = relationship('Events', back_populates='company', cascade="all, delete-orphan") 
