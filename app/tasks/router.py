from fastapi import APIRouter, Depends
from app.tasks.service import TaskService
from app.users.dependencies import get_current_user, get_current_admin_user
from app.users.users import Users

router = APIRouter(
    prefix='/tasks',
    tags=['Задачи'],
)


@router.get("/me")
async def get_tasks_me(user: Users = Depends(get_current_user)):
    return await TaskService.find_all(user_id=user.id)


@router.get("/all")
async def get_tasks_all(current_user: Users = Depends(get_current_admin_user)):
    return await TaskService.find_all()
