from pydantic import BaseModel, ConfigDict
from datetime import datetime

class Employee(BaseModel):
    id: int
    company_id: int | None = None
    firstname: str | None = None
    lastname: str | None = None
    status: str | None = None
    working_hours: int | None = None
    operating_time: datetime | None = None
    rest_time: datetime | None = None
    idle_time: datetime | None = None
    using_the_phone_time: datetime | None = None
    last_update_time: datetime | None = None

    model_config = ConfigDict(from_attributes=True)


