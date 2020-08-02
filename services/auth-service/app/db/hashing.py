from typing import Union

from sqlalchemy.orm import Session

from passlib.context import CryptContext

from . import models

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def encrypt_password(password: str) -> str:
    return pwd_context.hash(password)


def authenticate_user(
    db: Session, email: str, password: str
) -> Union[str, models.User]:
    user = db.query(models.User).filter(models.User.email == email).first()
    if not user or not verify_password(password, user.password):
        return False
    return user
