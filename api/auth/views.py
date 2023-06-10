from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from . import crud
from . import models
from .dependencies import get_user

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


@router.post("/login")
async def login(user: OAuth2PasswordRequestForm = Depends()) -> models.Token:
    user_db = await crud.user_login(user)
    token = crud.generate_token(user_db)
    return token


@router.get("/hi")
def hi(user: models.User = Depends(get_user)) -> str:
    if user:
        return f"Hello, {user.username}!"
    else:
        return "Hello world!"
