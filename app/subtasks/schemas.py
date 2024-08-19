from datetime import date

from pydantic import BaseModel


class SSubTask(BaseModel):
    id: int
    task_id: int
    title: str
    priority: str
    completed: bool

    class Config:
        orm_mode = True
