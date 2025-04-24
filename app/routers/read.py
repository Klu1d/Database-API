import crud
import database
import models
import schemas
from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()


@router.get("/read/companies", response_model=models.Company | list[models.Company])
async def read_company(
    session: AsyncSession = Depends(database.sessions), id: int = Query(None)
):
    companies = await crud.read(session=session, schema=schemas.Companies, id=id)
    return companies


@router.get("/read/employees", response_model=models.Employee | list[models.Employee])
async def read_employee(
    session: AsyncSession = Depends(database.sessions), id: int = Query(None)
):
    employees = await crud.read(session=session, schema=schemas.Employees, id=id)
    return employees


@router.get("/read/cameras", response_model=models.Camera | list[models.Camera])
async def read_cameras(
    session: AsyncSession = Depends(database.sessions), id: int = Query(None)
):
    cameras = await crud.read(session=session, schema=schemas.Cameras, id=id)
    return cameras


@router.get("/read/events", response_model=models.Event | list[models.Event])
async def read_event(
    session: AsyncSession = Depends(database.sessions), id: int = Query(None)
):
    events = await crud.read(session=session, schema=schemas.Events, id=id)
    return events
