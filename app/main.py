import datetime
from typing import List, Optional
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from app.tasks.router import router as router_tasks
from app.subtasks.router import router as router_subtasks
from app.users.router import router as router_users

app = FastAPI(
    title='My Notebook'
)

app.include_router(router_users)
app.include_router(router_tasks)
app.include_router(router_subtasks)

users = [
    {"id": 1, 'role': 'admin', 'name': 'Petr'},
    {"id": 2, 'role': 'user', 'name': 'Polina'},
    {"id": 3, 'role': 'user', 'name': 'Andrew'},
]


class User(BaseModel):
    id: int
    name: str
    role: Optional[str] = None


@app.get("/users/{user_id}", response_model=List[User])
def get_user(user_id: int):
    return [user for user in users if user.get('id') == user_id]


# Модель для подзадачи
class SubTask(BaseModel):
    id: int
    title: str
    completed: bool


# Модель для задач
class STask(BaseModel):
    id: int
    user_id: int
    title: str
    priority: str
    completed: bool
    date_to: Optional[datetime.date] = None
    subtasks: List[SubTask] = []  # Список подзадач, по умолчанию пуст


# Пример данных задач
tasks_list = [
    STask(
        id=1,
        user_id=1,
        title="Покормить кота",
        priority="medium",
        completed=False,
        date_to=datetime.date(2024, 8, 6),
        subtasks=[
            SubTask(id=1, title="Купить корм", completed=False),
            SubTask(id=2, title="Накормить кота", completed=False)
        ]
    ),
    STask(
        id=2,
        user_id=1,
        title="Почистить зубы",
        priority="low",
        completed=False,
        date_to=datetime.date(2024, 8, 6),
        subtasks=[]
    ),
    STask(
        id=3,
        user_id=2,
        title="Накраситься",
        priority="low",
        completed=False,
        date_to=datetime.date(2024, 8, 6),
        subtasks=[
            SubTask(id=1, title="Выбрать цвет", completed=False)
        ]
    ),
    STask(
        id=4,
        user_id=2,
        title="Подать документы на отпуск",
        priority="high",
        completed=False,
        date_to=datetime.date(2024, 8, 20),
        subtasks=[
            SubTask(id=1, title="Заполнить документ", completed=False),
            SubTask(id=2, title="Отправить документы на согласование", completed=False)
        ]
    ),
    STask(
        id=5,
        user_id=3,
        title="Провести митинг",
        priority="low",
        completed=False,
        date_to=datetime.date(2024, 8, 10),
        subtasks=[
            SubTask(id=1, title="Созвониться с коллегами", completed=False)
        ]
    ),
    STask(
        id=6,
        user_id=3,
        title="Пообедать",
        priority="low",
        completed=False,
        date_to=datetime.date(2024, 8, 10),
        subtasks=[
            SubTask(id=1, title="Купить еды в магазине", completed=False)
        ]
    ),
    STask(
        id=7,
        user_id=3,
        title="Собрать статистику работы сотрудников",
        priority="low",
        completed=False,
        date_to=datetime.date(2024, 8, 29),
        subtasks=[
            SubTask(id=1, title="Опросить каждого работника", completed=False),
            SubTask(id=2, title="Отфильтровать данные", completed=False),
            SubTask(id=3, title="Составить отчет", completed=False)
        ]
    ),
]


@app.get("/tasks_2")
def get_tasks_2(user_id: int, title: Optional[str] = None, priority: Optional[str] = None) -> List[STask]:
    # Фильтрация задач по user_id
    filtered_tasks = [task for task in tasks_list if task.user_id == user_id]

    # Дополнительно фильтруем по названию задачи, чтобы посмотреть подзадачи этой задачи
    if title:
        filtered_tasks = [task for task in tasks_list if task.title == title]
    # Если задан приоритет, фильтруем дополнительно
    if priority:
        filtered_tasks = [task for task in filtered_tasks if task.priority == priority]

    return filtered_tasks


@app.post("/add_task")
def add_task(task: STask):
    pass


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
