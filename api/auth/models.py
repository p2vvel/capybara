from beanie import Document
from datetime import datetime
from pydantic import BaseModel


# user model stored in database
class User(Document):
    username: str
    password: str
    is_superuser: bool = False
    is_pro_user: bool = False
    is_active: bool = True
    is_active: bool = True
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()


class UserInput(BaseModel):
    username: str
    password: str


class UserOutput(BaseModel):
    username: str
    is_superuser: bool
    is_pro_user: bool
    is_active: bool
    is_active: bool
    created_at: datetime
    updated_at: datetime


class Token(BaseModel):
    active_token: str
    token_type: str = "bearer"
    expires: int
