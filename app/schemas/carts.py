from pydantic import BaseModel, Field
from typing import List
from datetime import datetime
from app.schemas.products import ProductBase, CategoryBase


class BaseConfig:
    from_attributes = True


class ProductBaseCart(ProductBase):
    categrory: CategoryBase = Field(exclude=True)

    
    class Config(BaseConfig):
        pass


# base cart And cart item
class CartItemBase(BaseModel):
    id: int
    product_it: int
    quantity: int
    subtotal: float
    product: ProductBaseCart


class CartBase(BaseModel):
    id: int
    user_id: int
    created_at: datetime
    total_amount: float
    cart_items: List[CartItemBase]


    class Config(BaseConfig):
        pass


class CartOutBase(BaseModel):
    id: int
    user_id: int
    created_at: datetime
    total_amount: float
    cart_items: List[CartItemBase]


    class Config(BaseConfig):
        pass


# get cart
class CartOut(BaseModel):
    message: str
    data: CartBase


    class Config(BaseConfig):
        pass


class CartsOutList(BaseModel):
    message: str
    data: List[CartBase]


class CartUserOutList(BaseModel):
    message: str
    data: List[CartBase]


    class Config(BaseConfig):
        pass


# delete cart
class CartOutDelete(BaseModel):
    message: str
    data: CartOutBase


# create cart
class CartItemCreate(BaseModel):
    product_id: int
    quantity: int


class CartCreate(BaseModel):
    cart_items: List[CartItemCreate]


    class Config(BaseConfig):
        pass


# update cart
class CartUpdate(CartCreate):
    pass
