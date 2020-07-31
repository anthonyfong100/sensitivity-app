from pydantic import BaseModel


class UserAccountDetails(BaseModel):
    email: str
    password: str


class UserAccountCreateConfirm(UserAccountDetails):
    id: int
