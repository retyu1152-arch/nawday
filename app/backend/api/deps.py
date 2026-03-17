from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.backend.repositories.user_repository import UserRepository
from app.backend.utils.db import get_db
from app.backend.utils.security import decode_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/users/login")


def get_current_user_email(token: str = Depends(oauth2_scheme)) -> str:
    subject = decode_token(token)
    if not subject:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication token")
    return subject


def get_current_user(db: Session = Depends(get_db), email: str = Depends(get_current_user_email)):
    user = UserRepository(db).get_by_email(email)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")
    return user
