from fastapi import APIRouter, Depends
from app.tasks.service import TaskService
from app.users.dependencies import get_current_user
from app.users.users import Users

router = APIRouter(
    prefix='/tasks',
    tags=['Задачи'],
)


@router.get("")
async def get_tasks(user: Users = Depends(get_current_user)):
    return await TaskService.find_all(user_id=user.id)
