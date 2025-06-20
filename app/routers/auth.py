from fastapi import APIRouter, Depends, status, Header
from sqlalchemy.orm import Session
from app.services.auth import AuthService
from app.db.database import get_db
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from app.schemas.auth import UserOut, SignUp, TokenResponse


router = APIRouter(tags=["Auth"], prefix="/auth")


@router.post(
    "/signup",
    status_code=status.HTTP_200_OK,
    response_model=UserOut,
)
async def user_signup(
    user: SignUp,
    db: Session = Depends(get_db)
):
    return await AuthService.signup(db=db, user=user)

@router.post(
    "/login",
    status_code=status.HTTP_200_OK,
    response_model=TokenResponse,
)
async def user_login(
    user_credentials: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    return await AuthService.login(user_credentials=user_credentials, db=db)

@router.post(
    "/refresh",
    status_code=status.HTTP_200_OK,
)
async def refresh_access_token(
    refresh_token: str = Header(),
    db: Session = Depends(get_db)
    ):
    return await AuthService.get_refresh_token(token=refresh_token, db=db)