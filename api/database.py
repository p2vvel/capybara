from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from api.config import MONGO_URI, MONGO_DB
from api.auth.models import User


async def init_db():
    client = AsyncIOMotorClient(MONGO_URI)
    await init_beanie(
        database=client.get_database(MONGO_DB),
        document_models=[User],     # TODO: Update models here
    )
