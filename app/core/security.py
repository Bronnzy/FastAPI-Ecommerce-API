from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
from app.core.config import settings
from jose import JWTError, jwt
from app.schemas.auth import TokenResponse
from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException, Depends, status
from app.models.models import User
from sqlalchemy.orm import Session
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.db.database import get_db
from app.utils.responses import ResponseHandler


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
auth_scheme = HTTPBearer()

# Create hash password
def get_password_hash(password):
    return pwd_context.hash(password)

# Verify hash password
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

# Create Access and Refresh Token
async def get_user_token(id: int, refresh_token=None):
    payload = {"id": id}
    access_token_expiry = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = await create_access_token(payload, access_token_expiry)

    if not refresh_token:
        refresh_token = await create_refresh_token(payload)

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "Bearer",
        "expires_in": settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60
    }
# Create Access Token
async def create_access_token(data: dict, access_token_expiry=None):
    payload = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    payload.update({"exp": expire})

    return jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

# Create Refresh Token
async def create_refresh_token(data):
    return jwt.encode(data, settings.SECRET_KEY, settings.ALGORITHM)

# Get Payload of Token
def get_token_payload(token):
    try:
        return jwt.decode(token, settings.SECRET_KEY, [settings.ALGORITHM])
    except JWTError:
        raise ResponseHandler.invalid_token("access")
    
def get_current_user(token):
    user = get_token_payload(token.credentials)
    return user.get("id")

def check_admin_role(
    token: HTTPAuthorizationCredentials = Depends(auth_scheme),
    db: Session = Depends(get_db)
    ):
    user = get_token_payload(token.credentials)
    user_id = user.get("id")
    role_user = db.query(User).filter(User.id == user_id).first()
    if role_user.role != "admin":
        raise HTTPException(status_code=403, detail="Admin role required")