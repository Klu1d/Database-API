from sqlalchemy import Column, Integer, String, DateTime, JSON, ForeignKey, ARRAY, Time
from sqlalchemy.orm import relationship
from database import Base


class Cameras(Base):
    __tablename__        = "cameras"
    id                   = Column(Integer, primary_key=True, autoincrement=True, unique=True)
    name                 = Column(String)
    rtsp                 = Column(String)
    location_name        = Column(String, nullable=True)
    coordinate           = Column(ARRAY(Integer), nullable=True)
    company_id           = Column(Integer, ForeignKey('companies.id'))
    company              = relationship('Companies', back_populates='cameras')
    events               = relationship("Events", back_populates="camera")

