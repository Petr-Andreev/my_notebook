from datetime import date

from pydantic import BaseModel


class STask(BaseModel):
    id: int
    user_id: int
    title: str
    priority: str
    date_to: date
    completed: bool

    class Config:
        orm_mode = True
