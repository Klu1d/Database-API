from database import Base
from sqlalchemy import JSON, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Events(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    device_id = Column(String, nullable=True)
    camera_id = Column(Integer, ForeignKey("cameras.id"))
    company_id = Column(Integer, ForeignKey("companies.id"))
    date_start = Column(DateTime)
    date_end = Column(DateTime)
    hash = Column(String, nullable=True)
    video = Column(String, nullable=True)
    image = Column(String, nullable=True)
    details = Column(JSON)
    company = relationship("Companies", back_populates="events")
    camera = relationship("Cameras", back_populates="events")
