from pydantic import BaseModel, ConfigDict
from datetime import datetime


class Event(BaseModel):
    id: int
    device_id: str | None = None
    camera_id: int | None = None
    company_id: int | None = None
    date_start: datetime | None = None
    date_end: datetime | None = None
    hash: str | None = None     
    video: str | None = None    
    image: str | None = None    
    details: dict | None = None

    model_config = ConfigDict(from_attributes=True)
