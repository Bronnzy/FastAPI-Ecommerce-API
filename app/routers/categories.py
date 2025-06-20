from fastapi import APIRouter, Depends, Query, status
from app.db.database import get_db
from app.services.categories import CategoryService
from sqlalchemy.orm import Session
from app.schemas.categories import CategoryCreate, CategoryOut, CategoriesOut, CategoryOutDelete, CategoryUpdate
from app.core.security import check_admin_role


router = APIRouter(tags=["Categories"], prefix="/categories")


# get all categories
@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=CategoriesOut,
    )
def get_all_categories(
    db: Session = Depends(get_db),
    page: int = Query(1, ge=1, description="Page number"),
    limit: int = Query(10, ge=1, le=100, description="Items per page"),
    search: str | None = Query("", description="Search based on category names"),
):
    return CategoryService.get_all_categories(db=db, page=page, limit=limit, search=search)

# get category by id
@router.get(
    "/{category_id}",
    status_code=status.HTTP_200_OK,
    response_model=CategoryOut,
    )
def get_category(
    category_id: int,
    db: Session = Depends(get_db),
):
    return CategoryService.get_category(category_id=category_id, db=db)

# create new category
@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=CategoryOut,
    dependencies=[Depends(check_admin_role)],
    )
def create_category(
    category: CategoryCreate,
    db: Session = Depends(get_db),
):
    return CategoryService.create_category(category=category, db=db)

# update existing category
@router.put(
    "/{category_id}",
    status_code=status.HTTP_200_OK,
    response_model=CategoryOut,
    dependencies=[Depends(check_admin_role)],
)
def update_category(
    category_id: int,
    updated_category: CategoryUpdate,
    db: Session = Depends(get_db),
):
    return CategoryService.update_category(category_id=category_id, update_category=updated_category, db=db)

# delete category by id
@router.delete(
    "/{category_id}",
    status_code=status.HTTP_200_OK,
    response_model=CategoryOutDelete,
    dependencies=[Depends(check_admin_role)],
)
def delete_category(
    category_id: int,
    db: Session = Depends(get_db),
):
    return CategoryService.delete_category(category_id=category_id, db=db)