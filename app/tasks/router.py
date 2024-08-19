from fastapi import APIRouter

from app.tasks.schemas import STask
from app.tasks.service import TaskService

router = APIRouter(
    prefix='/tasks',
    tags=['Задачи'],
)


@router.get("")
async def get_tasks() -> list[STask]:
    return await TaskService.find_all()
