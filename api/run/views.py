from fastapi import APIRouter


router = APIRouter()


@router.get("/")
def get_run():
    return {"message": "Hello World"}
