from datetime import date
from typing import Optional

from pydantic import BaseModel


class STask(BaseModel):
    id: int
    user_id: int
    title: str
    priority: Optional[str] = 'medium'
    date_to: Optional[date]
    completed: Optional[bool] = False

    class Config:
        orm_mode = True
