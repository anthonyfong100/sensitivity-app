import os

from fastapi import Depends, HTTPException, status
from fastapi.security.http import HTTPAuthorizationCredentials, HTTPBearer
from jose import JWTError, jwt

auth = HTTPBearer()


async def verify_token(
    jwt_token: HTTPAuthorizationCredentials = Depends(auth),
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(
            jwt_token.credentials,
            os.getenv("SECRET_KEY"),
            algorithms=["HS256"],
        )
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        return username
    except (JWTError, KeyError):
        raise credentials_exception
