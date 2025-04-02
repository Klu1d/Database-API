from fastapi import APIRouter, Query, Depends
from sqlalchemy.ext.asyncio import AsyncSession

import database
import schemas
import models
import crud


router = APIRouter()

@router.get('/read/company', response_model=models.Company | list[models.Company])
async def read_company(
    session: AsyncSession = Depends(database.sessions), id: int = Query(None)
):
    company = await crud.read(session=session, schema=schemas.Companies, id=id)
    return company

@router.get('/read/employee', response_model=models.Employee | list[models.Employee])
async def read_employee(
    session: AsyncSession = Depends(database.sessions), id: int = Query(None)
):
    async for session in database.sessions():
        employees = await crud.read(session, schemas.Employees, id)
    return employees

@router.get('/read/camera', response_model=models.Camera | list[models.Camera])
async def read_cameras(
    session: AsyncSession = Depends(database.sessions), id: int = Query(None)
):
    async for session in database.sessions():
        cameras = await crud.read(session, schemas.Cameras, id)
    return cameras

@router.get('/read/event', response_model=models.Event | list[models.Event])
async def read_event(
    session: AsyncSession = Depends(database.sessions), id: int = Query(None)
):
    async for session in database.sessions():
        events = await crud.read(session, schemas.Events, id)
    return events
