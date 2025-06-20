from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import List
from app.schemas.carts import CartBase


# Reusable config base
class BaseConfig:
    from_attributes = True


class AccountBase(BaseModel):
    id: int
    username: str
    email: EmailStr
    full_name: str
    role: str
    is_active: bool
    created_at: datetime
    carts: List[CartBase]

    class Config(BaseConfig):
        pass


class AccountUpdate(BaseModel):
    username: str
    email: EmailStr
    full_name: str


class AccountOut(BaseModel):
    message: str
    data: AccountBase

    class Config(BaseConfig):
        pass
