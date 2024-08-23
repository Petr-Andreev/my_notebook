from datetime import date, datetime
from typing import Optional

from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from fastapi import APIRouter, Depends, Form, Request
from app.tasks.schemas import STask
from app.tasks.service import TaskService
from app.users.dependencies import get_current_user, get_current_admin_user
from app.users.users import Users
from exeptions import TaskAlreadyExistsException

router = APIRouter(
    prefix='/tasks',
    tags=['Задачи'],
)


@router.get("/my_tasks")
async def get_my_tasks(user: Users = Depends(get_current_user)) -> list[STask]:
    return await TaskService.find_all(user_id=user.id)


@router.get("/one_task_by_title/{task_title}")
async def get_my_tasks_by_title(task_title: str, user: Users = Depends(get_current_user)) -> STask:
    return await TaskService.find_one_or_none(title=task_title, user_id=user.id)


@router.get("/one_task_by_id/{task_id}")
async def get_my_tasks_by_id(task_id: int, user: Users = Depends(get_current_user)) -> STask:
    return await TaskService.find_one_or_none(id=task_id, user_id=user.id)


@router.get("/all")
async def get_all_tasks(current_user: Users = Depends(get_current_admin_user)) -> list[STask]:
    return await TaskService.find_all()


@router.post('/create')
async def add_my_task(
        task_data: STask,
        user: Users = Depends(get_current_user)
) -> STask:
    existing_title = await TaskService.find_one_or_none(title=task_data.title)
    if existing_title:
        raise TaskAlreadyExistsException
    await TaskService.add(
        title=task_data.title,
        priority=task_data.priority,
        date_to=task_data.date_to,
        completed=task_data.completed,
        user_id=user.id
    )
