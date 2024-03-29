from fastapi import APIRouter, Depends, HTTPException, status
from api.auth.dependencies import get_user_or_401
from api.auth.models import User
from .utils import start_dev_container, get_container, user_code_name, container_status, delete_container, container_edit
from .models import CodeStatus, ContainerEdit


router = APIRouter()


@router.post("/", response_model=CodeStatus)
def create_code_env(user: User = Depends(get_user_or_401)):
    ''' Create new container '''
    
    code = start_dev_container(user)
    return container_status(code)


@router.get("/", response_model=CodeStatus)
def get_code_env(user: User = Depends(get_user_or_401)):
    ''' Get container status'''
    code = get_container(user_code_name(user))
    return container_status(code)


@router.delete("/")
def delete_code_env(user: User = Depends(get_user_or_401)):
    ''' Delete container '''
    code = get_container(user_code_name(user))
    if code is not None:
        delete_container(code)
        raise HTTPException(status_code=status.HTTP_200_OK, detail="Container deleted")
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Container not created")


@router.put("/", response_model=None)
def update_code_env(state: ContainerEdit, user: User = Depends(get_user_or_401)):
    ''' Update container state, eg. available memory, state (stop, start, etc) '''
    code = get_container(user_code_name(user))
    container_edit(code, state)
    raise HTTPException(status_code=status.HTTP_200_OK, detail="Container updated")
