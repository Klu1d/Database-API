from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from database import Base


SINGULAR_NAMES = {
    "events": "Event",
    "employees": "Employee",
    "companies": "Company",
    "cameras": "Camera"
}

async def create(session: AsyncSession, schema: Base, id: int):
    session.add(schema)
    session.commit()
    session.refresh(schema)
    return schema


async def update(session: AsyncSession, schema: Base, id: int, params: dict):
    result = await session.execute(select(schema).filter(schema.id == id))
    record = result.scalars().first()

    if not record:
        raise ValueError(f"{schema.__name__} with ID {id} not found")

    # Обновляем только переданные параметры
    for key, value in params.items():
        if value is not None:
            setattr(record, key, value)

    session.add(record)
    await session.commit()
    return record


async def read(session: AsyncSession, schema: Base, id: int):
    result = await session.execute(
        select(schema)
        .where(schema.id == id)
        if id else select(schema)
    )
    record = (
        result.scalars().first()
        if id else result.scalars().all()
    )
    return record


async def delete(session: AsyncSession, schema: Base, id: int):
    company = await session.get(schema, id)

    if not company:
        raise HTTPException(404, f"{SINGULAR_NAMES[schema.__tablename__]} with id {id} not found")

    await session.delete(company)
    await session.commit()
    return {"message": f"{SINGULAR_NAMES[schema.__tablename__]} with id {id} has been deleted"}
