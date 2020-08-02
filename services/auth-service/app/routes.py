from datetime import datetime, timedelta

from sqlalchemy.orm import Session

from fastapi import APIRouter, Depends, HTTPException, Response, status
from fastapi.security import OAuth2PasswordRequestForm

from .auth import ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token
from .db import crud
from .db.database import get_db
from .db.hashing import authenticate_user
from .schema import Token, UserAccountCreateConfirm, UserAccountDetails

auth_router = APIRouter()


@auth_router.get("/healthcheck")
async def root():
    return Response(status_code=status.HTTP_200_OK)


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


@auth_router.post("/token", response_model=Token)
async def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    user = authenticate_user(
        db, form_data.username, form_data.password
    )  # the username here refers to the email

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
