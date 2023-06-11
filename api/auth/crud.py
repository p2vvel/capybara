from fastapi import status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta, datetime
from .models import User, UserInput, Token
from .utils import pwd_context
from .. import config
import jwt


async def create_user(user: UserInput) -> User:
    if await User.find(User.username == user.username).first_or_none():
        raise HTTPException(status_code=409, detail="Username already exists")
    else:
        hashed_password = pwd_context.hash(user.password)
        new_user = user.dict()
        new_user.update({"password": hashed_password})
        temp = User(**new_user)
        await temp.create()
        return temp


async def get_users() -> list[User]:
    result = await User.find_all().to_list()
    return result


async def get_user_by_username(username: str) -> User:
    user = await User.find(User.username == username).first_or_none()
    if user:
        return user
    else:
        raise HTTPException(status_code=404, detail="User not found")


async def update_user(username: str, user: UserInput) -> User:
    user_db = await User.find(User.username == username).first_or_none()
    if user_db:
        new_user = user.dict()
        new_user.update({"password": pwd_context.hash(user.password)})
        await user_db.set(new_user)
        user_db.update()
        return user_db
    else:
        raise HTTPException(status_code=404, detail="User not found")


async def delete_user(username: str) -> None:
    user = await User.find(User.username == username).first_or_none()
    if user:
        await user.delete()
    else:
        raise HTTPException(status_code=404, detail="User not found")


async def user_login(user: OAuth2PasswordRequestForm) -> User:
    user_db = await get_user_by_username(user.username)

    if user_db:
        if pwd_context.verify(user.password, user_db.password):
            return user_db
        else:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Wrong password")
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"User '{user.username}' not existing"
        )


def generate_token(user: UserInput, time_delta: timedelta = timedelta(minutes=15)) -> Token:
    expiration_time = (datetime.utcnow() + time_delta).timestamp()
    payload = {
        "sub": user.username,
        "iss": expiration_time,
    }

    token = jwt.encode(payload, config.SECRET, algorithm=config.ALGORITHM)
    return Token(active_token=token, expires=expiration_time)
