from sqlalchemy.orm import Session

from fastapi import APIRouter, Depends, HTTPException

from .db import crud
from .db.database import get_db
from .schema import UserAccountCreateConfirm, UserAccountDetails

auth_router = APIRouter()


@auth_router.get("/")
async def root():
    return {"message": "Hello World"}


@auth_router.post(
    "/users/", response_model=UserAccountCreateConfirm, status_code=201
)
async def create_user(
    payload: UserAccountDetails, db: Session = Depends(get_db)
):
    db_user = crud.get_user_by_email(db, email=payload.email)
    if db_user:
        raise HTTPException(
            status_code=400, detail="User has already registered"
        )

    user_created = crud.create_user(db=db, user=payload)

    response = {"id": user_created.id, **payload.dict()}

    return response
