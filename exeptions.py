from fastapi import HTTPException, status


class MyNotebookException(HTTPException):
    status_code = 500
    detail = ''

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class UserAlreadyExistsException(MyNotebookException):
    status_code = status.HTTP_409_CONFLICT
    detail = 'Пользователь с таким email уже зарегистрирован'


class IncorrectEmailOrPasswordException(MyNotebookException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = 'Неверный логин или пароль'


class TokenExpiredException(MyNotebookException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = 'Токен истек'


class TokenAbsentException(MyNotebookException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = 'Токен отсутствует'


class IncorrectFormatTokenException(MyNotebookException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = 'Неверный формат токена'


class UserIsNotPresentException(MyNotebookException):
    status_code = status.HTTP_401_UNAUTHORIZED


class UserDntHaveAccessException(MyNotebookException):
    status_code = status.HTTP_403_FORBIDDEN
    detail = 'Нет прав на просмотр'
