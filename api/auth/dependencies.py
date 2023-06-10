from fastapi import Depends, HTTPException, status
from .utils import oauth_scheme
from .crud import get_user_by_username
from .. import config
import jwt
from .models import User


async def get_user(token: str = Depends(oauth_scheme)) -> User | None:
    if token:
        payload = jwt.decode(token, config.SECRET, algorithms=[config.ALGORITHM])
        username = payload.get("sub")
        user = await get_user_by_username(username)
        return user
    else:
        return None


def get_user_or_401(user: User | None = Depends(get_user)) -> User:
    if user is not None:
        return user
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)


def get_admin_or_401(user: User | None = Depends(get_user_or_401)) -> User:
    if user.is_superuser:
        return user
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
