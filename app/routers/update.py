from datetime import datetime
from fastapi import APIRouter, Query, Body, Depends
from sqlalchemy.ext.asyncio import AsyncSession

import database
import models
import schemas
import crud


router = APIRouter()

@router.patch('/update/company/{id}', response_model=models.Company)
async def update_company(
    id: int,
    name: str = Query(None),
    password: str = Query(None),
    email: str = Query(None),
    session: AsyncSession = Depends(database.sessions)
):
    params = dict(locals())
    params.pop('id')
    company = await crud.update(
        id=id,
        params=params,
        session=session,
        schema=schemas.Companies, 
    )
    return company

@router.patch('/update/employee/{id}', response_model=models.Employee)
async def update_employee(
    id: int, 
    firstname: str = Query(None),
    lastname: str = Query(None),
    status: str = Query(None),
    working_hours: int = Query(None),
    operating_time: datetime = Query(None),
    rest_time: datetime = Query(None),
    idle_time: datetime = Query(None),
    using_the_phone_time: datetime = Query(None),
    last_update_time: datetime = Query(None),
    session: AsyncSession = Depends(database.sessions)
):
    params = dict(locals())
    params.pop('id')
    employee = await crud.update(
        id=id, 
        params=params,
        session=session,
        schema=schemas.Employees 
    )
    return employee

@router.patch('/update/camera/{id}', response_model=models.Camera)
async def update_camera(
    id: int,
    name: str = Query(None),
    rtsp: str = Query(None),
    location_name: str = Query(None),
    coordinate: list[int] = Query(None),
    session: AsyncSession = Depends(database.sessions)
):
    params = dict(locals())
    params.pop('id')
    camera = await crud.update(
        id=id,
        params=params, 
        session=session,
        schema=schemas.Cameras
    )
    return camera

@router.patch('/update/event/{id}', response_model=models.Event)
async def update_event(
    id: int,
    device_id: str = Query(None),
    camera_id: int = Query(None),
    hash: str = Query(None),
    video: str = Query(None),
    image: str = Query(None),
    date_start: datetime = Query(None),
    date_end: datetime = Query(None),
    details: dict = Body(None),
    session: AsyncSession = Depends(database.sessions)
):
    params = dict(locals())
    params.pop('id')
    event = await crud.update(
        id=id,
        params=params,
        session=session,
        schema=schemas.Events,
    )
    return event