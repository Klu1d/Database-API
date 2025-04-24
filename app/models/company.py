from pydantic import BaseModel, ConfigDict


class Company(BaseModel):
    id: int
    name: str | None = None
    password: str | None = None
    email: str | None = None

    model_config = ConfigDict(from_attributes=True)
