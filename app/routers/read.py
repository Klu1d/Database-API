import crud
import database
import models
import schemas
from auth import secret
from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()


@router.get("/company", response_model=models.Company | list[models.Company])
async def read_company(
    session: AsyncSession = Depends(database.sessions), id: int = Query(None), api_key: str = Depends(secret)
):
    companies = await crud.read(session=session, schema=schemas.Companies, id=id)
    return companies


@router.get("/employee", response_model=models.Employee | list[models.Employee])
async def read_employee(
    session: AsyncSession = Depends(database.sessions), id: int = Query(None), api_key: str = Depends(secret)
):
    employees = await crud.read(session=session, schema=schemas.Employees, id=id)
    return employees


@router.get("/camera", response_model=models.Camera | list[models.Camera])
async def read_cameras(
    session: AsyncSession = Depends(database.sessions), id: int = Query(None), api_key: str = Depends(secret)
):
    cameras = await crud.read(session=session, schema=schemas.Cameras, id=id)
    return cameras


@router.get("/event", response_model=models.Event | list[models.Event])
async def read_event(
    session: AsyncSession = Depends(database.sessions), id: int = Query(None), api_key: str = Depends(secret)
):
    events = await crud.read(session=session, schema=schemas.Events, id=id)
    return events
