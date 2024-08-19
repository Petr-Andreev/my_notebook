from passlib.context import CryptContext

pwb_context = CryptContext(schemes=["bcrypt"], deprecated='auto')


def get_password_hash(password: str) -> str:
    return pwb_context.hash(password)


def verify_password(plain_password, hashed_password) -> bool:
    return pwb_context.verify(plain_password, hashed_password)
