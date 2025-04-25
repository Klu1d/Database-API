import crud
import database
import schemas
from auth import secret
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()


@router.delete("/delete/company/{id}")
async def delete_company(id: int, session: AsyncSession = Depends(database.sessions), api_key: str = Depends(secret)):
    message = await crud.delete(session, schemas.Companies, id)
    return message


@router.delete("/delete/employee/{id}")
async def delete_employee(id: int, session: AsyncSession = Depends(database.sessions), api_key: str = Depends(secret)):
    message = await crud.delete(session, schemas.Employees, id)
    return message


@router.delete("/delete/camera/{id}")
async def delete_cameras(id: int, session: AsyncSession = Depends(database.sessions), api_key: str = Depends(secret)):
    message = await crud.delete(session, schemas.Cameras, id)
    return message


@router.delete("/delete/event/{id}")
async def delete_event(id: int, session: AsyncSession = Depends(database.sessions), api_key: str = Depends(secret)):
    message = await crud.delete(session, schemas.Events, id)
    return message
