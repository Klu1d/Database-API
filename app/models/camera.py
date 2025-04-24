from pydantic import BaseModel, ConfigDict


class Camera(BaseModel):
    id: int
    company_id: int | None = None
    name: str | None = None
    rtsp: str | None = None
    location_name: str | None = None
    coordinate: list[int] | None = None

    model_config = ConfigDict(from_attributes=True)
