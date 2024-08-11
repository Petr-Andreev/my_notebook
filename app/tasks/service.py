from app.services.base import BaseService
from app.tasks.tasks import Tasks


class TaskService(BaseService):
    model = Tasks

