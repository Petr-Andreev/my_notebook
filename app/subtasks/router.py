from fastapi import APIRouter
from app.subtasks.schemas import SSubTask
from app.subtasks.service import SubTaskService

router = APIRouter(
    prefix='/subtasks',
    tags=['Подзадачи'],
)


@router.get("")
async def get_subtasks() -> list[SSubTask]:
    return await SubTaskService.find_all()
