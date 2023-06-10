from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from api.config import MONGO_URI, MONGO_DB
from api.auth.models import User
from .auth.views import router as auth_router

# async def init_db():


# init_db()
app = FastAPI()
app.include_router(auth_router, prefix="/auth")


@app.get("/")
def root():
    return "Hello!"


@app.on_event("startup")
async def startup():
    client = AsyncIOMotorClient(MONGO_URI)
    
    await init_beanie(
        database=client.get_database(MONGO_DB),
        document_models=[User],     # TODO: Update models here
    )
