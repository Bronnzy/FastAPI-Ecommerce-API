from pydantic import BaseModel, field_validator
from datetime import datetime
from typing import List, Optional, ClassVar
from app.schemas.categories import CategoryBase


class BaseConfig:
    from_attributes = True


class ProductBase(BaseModel):
    id: int
    title: str
    description: Optional[str]
    price: int

    @field_validator("discount_percentage")
    def validate_discount_percentage(cls, discount_percentage):
        if discount_percentage < 0 or discount_percentage > 100:
            raise ValueError("discount_percentage must be between 0 and 100")
        return discount_percentage
    
    discount_percentage: float
    rating: float
    stock: int
    brand: str
    thumbnail: str
    images: List[str]
    is_published: bool
    created_at: datetime
    category_id: int
    category: CategoryBase


    class Config(BaseConfig):
        pass


# create product
class ProductCreate(ProductBase):
    id: ClassVar[int]
    category: ClassVar[CategoryBase]


    class Config(BaseConfig):
        pass

    
# update product
class ProductUpdate(ProductCreate):
    pass


# get products
class ProductOut(BaseModel):
    message: str
    data: ProductBase


    class Config(BaseConfig):
        pass


class ProductsOut(BaseModel):
    message: str
    data: List[ProductBase]

    class Config(BaseConfig):
        pass


# delete product
class ProductDelete(ProductBase):
    category: ClassVar[CategoryBase]


class ProductOutDelete(BaseModel):
    message: str
    data: ProductDelete