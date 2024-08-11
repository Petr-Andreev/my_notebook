from fastapi import APIRouter
from app.subtasks.service import SubTaskService

router = APIRouter(
    prefix='/subtasks',
    tags=['Подзадачи'],
)


@router.get("")
async def get_subtasks():
    return await SubTaskService.find_all()
