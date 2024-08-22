from fastapi import APIRouter, HTTPException, status, Response, Depends

from app.users.auth import get_password_hash, authenticate_user, create_access_token
from app.users.dao import UsersDAO
from app.users.dependencies import get_current_user, get_current_admin_user
from app.users.schemas import SUserRegister, SUserLogin
from app.users.users import Users

router = APIRouter(
    prefix='/auth',
    tags=['Auth & Пользователи'],
)


@router.post("/register")
async def register_user(user_data: SUserRegister):
    existing_user = await UsersDAO.find_one_or_none(email=user_data.email)
    if existing_user:
        raise HTTPException(status_code=500, detail='Пользователь с таким email уже зарегистрирован')
    hashed_password = get_password_hash(user_data.password)
    await UsersDAO.add(
        first_name=user_data.first_name,
        last_name=user_data.last_name,
        email=user_data.email,
        hashed_password=hashed_password)


@router.post("/login")
async def login_user(response: Response, user_data: SUserLogin):
    user = await authenticate_user(user_data.email, user_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Неверный логин или пароль.')
    access_token = create_access_token({"sub": str(user.id)})
    response.set_cookie('notebook_access_token', access_token, httponly=True)
    return {"access_token": access_token}


@router.post("/logout")
async def logout_user(response: Response):
    response.delete_cookie('notebook_access_token')
    return "Вы вышли из системы"


@router.get("/my_info")
async def read_users_me(current_user: Users = Depends(get_current_user)):
    return current_user


@router.get("/all_users_info")
async def read_users_all(current_user: Users = Depends(get_current_admin_user)):
    return await UsersDAO.find_all()
