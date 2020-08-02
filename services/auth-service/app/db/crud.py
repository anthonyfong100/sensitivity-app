from sqlalchemy.orm import Session

from app.schema import UserAccountDetails

from . import models
from .hashing import encrypt_password


def create_user(db: Session, user: UserAccountDetails) -> models.User:
    fake_hashed_password = encrypt_password(user.password)
    db_user = models.User(email=user.email, password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user_by_email(db: Session, email: str):

    user = db.query(models.User).filter(models.User.email == email).first()

    print(user)
    return user
