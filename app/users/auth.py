from datetime import datetime, timedelta

from jose import jwt
from passlib.context import CryptContext
from pydantic import EmailStr

from app.config import settings
from app.users.dao import UsersDAO

pwb_context = CryptContext(schemes=["bcrypt"], deprecated='auto')


def get_password_hash(password: str) -> str:
    return pwb_context.hash(password)


def verify_password(plain_password, hashed_password) -> bool:
    return pwb_context.verify(plain_password, hashed_password)


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=60)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.SICRET_KEY, settings.ALGORITHM
    )
    return encoded_jwt


async def authenticate_user(email: EmailStr, password: str):
    user = await UsersDAO.find_one_or_none(email=email)
    if not user and not verify_password(password, user.password):
        return None
    return user
