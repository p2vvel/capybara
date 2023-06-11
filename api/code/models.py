from pydantic import BaseModel


class CodeStatus(BaseModel):
    status: str
    name: str | None
    url: str | None
