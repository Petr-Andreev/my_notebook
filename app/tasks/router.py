from fastapi import APIRouter
from app.tasks.service import TaskService

router = APIRouter(
    prefix='/tasks',
    tags=['Задачи'],
)


@router.get("")
async def get_tasks():
    return await TaskService.find_all()
