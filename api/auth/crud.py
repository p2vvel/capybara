from .models import User, UserInput
from fastapi import HTTPException


async def create_user(user: UserInput) -> User:
    temp = User(**user.dict())
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
        await user_db.set(user.dict())
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
