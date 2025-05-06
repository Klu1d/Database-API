from contextlib import asynccontextmanager

import uvicorn
from database import Base, engine
from fastapi import FastAPI
from routers import create, read, update, delete, media


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(title="Database API", lifespan=lifespan)

app.include_router(create.router, tags=['Create'], prefix='/create')
app.include_router(read.router, tags=['Read'], prefix='/read')
app.include_router(update.router, tags=['Update'], prefix='/update')
app.include_router(delete.router, tags=['Delete'], prefix='/delete')
app.include_router(media.router, tags=['Media'], prefix='/media')

@app.get("/ping", include_in_schema=False)
async def ping():
    return {"status": "Database-API is running"}

if __name__ == "__main__":
    uvicorn.run(app)
