from fastapi import APIRouter, Depends
from app.subtasks.service import SubTaskService
from app.tasks.router import get_tasks_me
from app.tasks.tasks import Tasks

router = APIRouter(
    prefix='/subtasks',
    tags=['Подзадачи'],
)


@router.get("/me")
async def get_subtasks(tasks: Tasks = Depends(get_tasks_me)):
    return await SubTaskService.find_all()
