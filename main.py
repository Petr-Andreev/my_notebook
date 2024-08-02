from enum import Enum
from typing import List

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title='My Notebook'
)

users = [
    {"id": 1, 'role': 'admin', 'name': 'Petr'},
    {"id": 2, 'role': 'user', 'name': 'Polina'},
    {"id": 3, 'role': 'user', 'name': 'Andrew'},
]


class User(BaseModel):
    id: int
    role: str
    name: str


@app.get("/users/{user_id}", response_model=List[User])
def get_user(user_id: int):
    return [user for user in users if user.get('id') == user_id]


tasks_list = [
    {"id": 1, "user_id": 1, "title": "Покормить кота", "priority": "medium"},
    {"id": 2, "user_id": 1, "title": "Почистить зубы", "priority": "low"},
    {"id": 3, "user_id": 2, "title": "Накраситься", "priority": "low"},
    {"id": 4, "user_id": 2, "title": "Подать документы на отпуск", "priority": "high"},
    {"id": 5, "user_id": 3, "title": "Провести митинг", "priority": "medium"},
    {"id": 6, "user_id": 3, "title": "Пообедать", "priority": "high"},
    {"id": 7, "user_id": 3, "title": "Собрать статистику работы сотрудников", "priority": "high"},
]


class Priority(Enum):
    low_priority = "low"
    medium_priority = "medium"
    high_priority = "high"


class Task(BaseModel):
    id: int
    user_id: int
    title: str
    priority: Priority


@app.post('/tasks/create')
def add_task(tasks: List[Task]):
    tasks_list.extend(tasks)
    return {'status': 200, 'data': tasks_list}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
