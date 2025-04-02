import os

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from dotenv import load_dotenv


load_dotenv()

DB_HOST=os.getenv('DB_HOST')
DB_PORT=os.getenv('DB_PORT')
DB_USER=os.getenv('DB_USER')
DB_PASS=os.getenv('DB_PASS')
DB_NAME=os.getenv('DB_NAME')

URL = f'postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

engine = create_async_engine(URL, echo=True)

Session = sessionmaker(
    bind=engine, 
    class_=AsyncSession, 
    expire_on_commit=False, 
    autoflush=True
)

async def sessions():
    async with Session() as session:
        yield session

class Base(DeclarativeBase):
    pass
