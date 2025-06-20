from fastapi import APIRouter, Depends, Query, status
from app.db.database import get_db
from app.services.products import ProductService
from sqlalchemy.orm import Session
from app.schemas.products import ProductCreate, ProductOut, ProductsOut, ProductOutDelete, ProductUpdate
from app.core.security import get_current_user, check_admin_role


router = APIRouter(tags=["Products"], prefix="/products")

# get all products
@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=ProductOut,
)
def get_all_products(
    db: Session = Depends(get_db),
    page: int = Query(1, ge=1, description="Page number"),
    limit: int = Query(1, ge=1, le=100, description="Items per page"),
    search: str | None = Query("", description="Search based title of products"),
):
    return ProductService.get_all_products(db=db, page=page, limit=limit, search=search)


# get product by id
@router.get(
    "/{product_id}",
    status_code=status.HTTP_200_OK,
    response_model=ProductOut,
    dependencies=[Depends(check_admin_role)],
)
def get_product(
    product_id: int,
    db: Session = Depends(get_db),
):
    return ProductService.get_product(product_id=product_id, db=db)

# create new product
@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=ProductOut,
    dependencies=[Depends(check_admin_role)],
)
def create_product(
    product: ProductCreate,
    db: Session = Depends(get_db),
):
    return ProductService.create_product(product=product, db=db)

# update existing product
@router.put(
    "/{product_id}",
    status_code=status.HTTP_200_OK,
    response_model=ProductOut,
    dependencies=[Depends(check_admin_role)],
)
def update_product(
    product_id: int,
    updated_product: ProductUpdate,
    db: Session = Depends(get_db),
):
    return ProductService.update_product(product_id=product_id, updated_product=updated_product, db=db)

# delete product by id
@router.delete(
    "/{product_id}",
    status_code=status.HTTP_200_OK,
    response_model=ProductOutDelete,
    dependencies=[Depends(check_admin_role)],
)
def delete_product(
    product_id: int,
    db: Session = Depends(get_db),
):
    return ProductService.delete_product(product_id=product_id, db=db)
