from app.services.base import BaseService
from app.users.users import Users


class UsersDAO(BaseService):
    model = Users
