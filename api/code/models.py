from pydantic import BaseModel
from enum import Enum


class CodeStatus(BaseModel):
    status: str
    name: str | None
    url: str | None


class CodeStateCommandEnum(str, Enum):
    START = "start"
    STOP = "stop"
    RESTART = "restart"


class ContainerEdit(BaseModel):
    state: CodeStateCommandEnum | None
