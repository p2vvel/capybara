from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from api.config import MONGO_URI, MONGO_DB
from api.auth.models import User
from .auth.views import router as auth_router
from .code.views import router as code_router
from .run.views import router as run_router


app = FastAPI()
app.include_router(auth_router, prefix="/auth")
app.include_router(code_router, prefix="/code")
app.include_router(run_router, prefix="/run")


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
