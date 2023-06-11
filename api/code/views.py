from fastapi import APIRouter, Depends, HTTPException, status
from api.auth.dependencies import get_user_or_401
from api.auth.models import User


router = APIRouter()


@router.post("/code")
def create_code_env(user: User = Depends(get_user_or_401)):
    return {"code": "1234"}


@router.get("/code")
def get_code_env(user: User = Depends(get_user_or_401)):
    return {"code": "1234"}


@router.delete("/code")
def delete_code_env(user: User = Depends(get_user_or_401)):
    return {"code": "1234"}


@router.put("/code")
def update_code_env(user: User = Depends(get_user_or_401)):
    return {"code": "1234"}
