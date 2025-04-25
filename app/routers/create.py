from datetime import datetime

import database
import models
import schemas
from auth import secret
from fastapi import APIRouter, Body, Depends, HTTPException, Query
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()


@router.post("/create/company", response_model=models.Company)
async def create_company(
    name: str = Query(),
    password: str = Query(),
    email: str = Query(None),
    session: AsyncSession = Depends(database.sessions),
    api_key: str = Depends(secret)
):
    try:
        company = schemas.Companies(name=name, password=password, email=email)
        session.add(company)
        await session.commit()
        await session.refresh(company)
    except IntegrityError:
        await session.rollback()
        raise HTTPException(status_code=409)
    return company


@router.post("/create/employee", response_model=models.Employee)
async def create_employee(
    company_id: int = Query(),
    firstname: str = Query(),
    lastname: str = Query(None),
    status: str = Query(None),
    working_hours: int = Query(None),
    operating_time: datetime = Query(None),
    rest_time: datetime = Query(None),
    idle_time: datetime = Query(None),
    using_the_phone_time: datetime = Query(None),
    last_update_time: datetime = Query(None),
    session: AsyncSession = Depends(database.sessions),
):
    company = await session.get(schemas.Companies, company_id)
    if not company:
        raise HTTPException(
            status_code=400, detail=f"Company with id {company_id} does not exist"
        )

    employee = schemas.Employees(
        firstname=firstname,
        lastname=lastname,
        status=status,
        working_hours=working_hours,
        operating_time=operating_time,
        rest_time=rest_time,
        idle_time=idle_time,
        using_the_phone_time=using_the_phone_time,
        last_update_time=last_update_time,
        company_id=company_id,
    )
    session.add(employee)
    await session.commit()
    await session.refresh(employee)
    return employee


@router.post("/create/camera", response_model=models.Camera)
async def create_camera(
    company_id: int = Query(),
    name: str = Query(),
    rtsp: str = Query(),
    location_name: str = Query(None),
    coordinate: list[int] = Query(None),
    session: AsyncSession = Depends(database.sessions),
):
    company = await session.get(schemas.Companies, company_id)
    if not company:
        raise HTTPException(
            status_code=400, detail=f"Company with id {company_id} does not exist"
        )

    camera = schemas.Cameras(
        company_id=company_id,
        name=name,
        rtsp=rtsp,
        location_name=location_name,
        coordinate=coordinate,
    )
    session.add(camera)
    await session.commit()
    await session.refresh(camera)
    return camera


@router.post("/create/event", response_model=models.Event)
async def create_event(
    device_id: str = Query(None),
    camera_id: int = Query(),
    company_id: int = Query(),
    hash: str = Query(None),
    video: str = Query(None),
    image: str = Query(None),
    date_start: datetime = Query(),
    date_end: datetime = Query(),
    details: dict = Body(),
    session: AsyncSession = Depends(database.sessions),
):
    company = await session.get(schemas.Companies, company_id)
    if not company:
        raise HTTPException(
            status_code=400, detail=f"Company with id {company_id} does not exist"
        )

    event = schemas.Events(
        device_id=device_id,
        camera_id=camera_id,
        company_id=company_id,
        hash=hash,
        video=video,
        image=image,
        date_start=date_start,
        date_end=date_end,
        details=details,
    )
    session.add(event)
    await session.commit()
    await session.refresh(event)
    return event
