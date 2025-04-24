from contextlib import asynccontextmanager

import uvicorn
from database import Base, engine
from fastapi import FastAPI
from routers import create, delete, read, update


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(
    title="Database API",
    docs_url="/database/api",
    lifespan=lifespan,
)

app.include_router(create.router)
app.include_router(read.router)
app.include_router(update.router)
app.include_router(delete.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8084)
