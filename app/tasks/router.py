from fastapi import APIRouter

router = APIRouter(
    prefix='/tasks',
    tags=['Задачи'],
)


@router.get('')
def get_tasks_2():
    pass


@router.get('/{task_id}')
def get_task(task_id):
    pass
