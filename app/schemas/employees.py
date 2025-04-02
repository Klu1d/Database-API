from sqlalchemy import Column, Integer, String, DateTime, JSON, ForeignKey, ARRAY, Time
from sqlalchemy.orm import relationship
from database import Base


class Employees(Base):
    __tablename__        = "employees"
    id                   = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    firstname            = Column(String)
    lastname             = Column(String, nullable=True)
    status               = Column(String, nullable=True)
    working_hours        = Column(Integer, nullable=True)
    operating_time       = Column(DateTime(timezone=True), nullable=True)
    rest_time            = Column(DateTime(timezone=True), nullable=True)
    idle_time            = Column(DateTime(timezone=True), nullable=True)
    using_the_phone_time = Column(DateTime(timezone=True), nullable=True)
    last_update_time     = Column(DateTime(timezone=True), nullable=True)
    company_id           = Column(Integer, ForeignKey('companies.id'))
    company              = relationship('Companies', back_populates='employees')