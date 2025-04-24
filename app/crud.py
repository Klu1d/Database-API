from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from database import Base


SINGULAR_NAMES = {
    "events": "Event",
    "employees": "Employee",
    "companies": "Company",
    "cameras": "Camera"
}


async def update(session: AsyncSession, schema: Base, id: int, params: dict):
    try:
        record = await session.get(schema, id)

        for key, value in params.items():
            if value is not None:
                setattr(record, key, value)

        session.add(record)
        await session.commit()
    except AttributeError:
        raise HTTPException(400, f"{SINGULAR_NAMES[schema.__tablename__]} with id {id} not found")
    except IntegrityError:
        raise HTTPException(409, "This name is already in use")
    return record


async def read(session: AsyncSession, schema: Base, id: int = None):
    query = select(schema)
    if id:
        query = query.where(schema.id == id)

    result = await session.execute(query)
    record = result.scalars().first() if id else result.scalars().all()

    return record


async def delete(session: AsyncSession, schema: Base, id: int):
    company = await session.get(schema, id)

    if not company:
        raise HTTPException(404, f"{SINGULAR_NAMES[schema.__tablename__]} with id {id} not found")

    await session.delete(company)
    await session.commit()
    return {"message": f"{SINGULAR_NAMES[schema.__tablename__]} with id {id} has been deleted"}