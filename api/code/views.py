from fastapi import APIRouter, Depends, HTTPException, status
from api.auth.dependencies import get_user_or_401
from api.auth.models import User
from api import containers

router = APIRouter()


@router.post("/code")
def create_code_env(user: User = Depends(get_user_or_401)):
    # create new container
    code = containers.start_dev_container()
    return {"code": "1234"}


@router.get("/code")
def get_code_env(user: User = Depends(get_user_or_401)):
    # get container status
    return {"code": "1234"}


@router.delete("/code")
def delete_code_env(user: User = Depends(get_user_or_401)):
    # delete container
    return {"code": "1234"}


@router.put("/code")
def update_code_env(user: User = Depends(get_user_or_401)):
    # update container state, eg. available memory, state (stop, start, etc)
    return {"code": "1234"}
