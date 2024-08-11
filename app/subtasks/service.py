from app.services.base import BaseService
from app.tasks.tasks import SubTasks


class SubTaskService(BaseService):
    model = SubTasks
