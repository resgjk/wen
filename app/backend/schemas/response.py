from pydantic import BaseModel


class SimpleResponse(BaseModel):
    response: str
