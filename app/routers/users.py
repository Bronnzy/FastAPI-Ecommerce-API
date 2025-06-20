from fastapi import APIRouter, Depends, Query, status
from app.db.database import get_db
from app.services.users import UserService
from sqlalchemy.orm import Session
from app.schemas.users import UserCreate, UserOut, UsersOut, UserOutDelete, UserUpdate
from app.core.security import check_admin_role


router = APIRouter(tags=["Users"], prefix="/users")


# get all users
@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=UsersOut,
    dependencies=[Depends(check_admin_role)],
)
def get_all_users(
    db: Session = Depends(get_db),
    page: int = Query(1, ge=1, description="Page number"),
    limit: int = Query(10, ge=1, le=100, description="Items per page"),
    search: str | None = Query("", description="Search based on username"),
    role: str = Query("user", enum=["user", "admin"])
):
    return UserService.get_all_users(db=db, page=page, limit=limit, search=search, role=role)

# get user by id
@router.get(
    "/{user_id}",
    status_code=status.HTTP_200_OK,
    response_model=UserOut,
    dependencies=[Depends(check_admin_role)],
)
def get_user(
    user_id: int,
    db: Session = Depends(get_db),
):
    return UserService.get_user(user_id=user_id, db=db)

# create new user
@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=UserOut,
    dependencies=[Depends(check_admin_role)],
)
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db),
):
    return UserService.create_user(user=user, db=db)

# update existing user
@router.put(
    "/{user_id}",
    status_code=status.HTTP_200_OK,
    response_model=UserOut,
    dependencies=[Depends(check_admin_role)],
)
def update_user(
    user_id: int,
    updated_user: UserUpdate,
    db: Session = Depends(get_db),
):
    return UserService.update_user(db=db, user_id=user_id, updated_user=updated_user)

# delete user by id
@router.delete(
    "/{user_id}",
    status_code=status.HTTP_200_OK,
    response_model=UserOutDelete,
    dependencies=[Depends(check_admin_role)],
)
def delete_user(
    user_id: int,
    db: Session = Depends(get_db),
):
    return UserService.delete_user(db=db, user_id=user_id)
