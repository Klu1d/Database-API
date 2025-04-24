import crud
import database
import schemas
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()


@router.delete("/delete/company/{id}")
async def update_company(id: int, session: AsyncSession = Depends(database.sessions)):
    message = await crud.delete(session, schemas.Companies, id)
    return message


@router.delete("/delete/employee/{id}")
async def update_employee(id: int, session: AsyncSession = Depends(database.sessions)):
    message = await crud.delete(session, schemas.Employees, id)
    return message


@router.delete("/delete/camera/{id}")
async def update_cameras(id: int, session: AsyncSession = Depends(database.sessions)):
    message = await crud.delete(session, schemas.Cameras, id)
    return message


@router.delete("/delete/event/{id}")
async def update_event(id: int, session: AsyncSession = Depends(database.sessions)):
    message = await crud.delete(session, schemas.Events, id)
    return message
