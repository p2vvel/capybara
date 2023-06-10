from fastapi import APIRouter, HTTPException
from . import crud
from . import models


router = APIRouter()


@router.post("/")
async def create_user(user: models.UserInput) -> models.UserOutput:
    result = await crud.create_user(user)
    return result


@router.get("/")
async def get_users() -> list[models.UserOutput]:
    return await crud.get_users()


@router.delete("/{username}")
async def delete_user(username: str) -> None:
    await crud.delete_user(username)
    raise HTTPException(status_code=200)


@router.put("/{username}")
async def update_user(username: str, user: models.UserInput) -> models.UserOutput:
    result = await crud.update_user(username, user)
    return result
