"""Reusable API dependencies."""
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.backend.models.base import get_db
from app.backend.models.user_model import User
from app.backend.repositories.user_repository import UserRepository
from app.backend.services.auth_service import AuthService

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/users/login")


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
) -> User:
    """Resolve currently authenticated user from bearer token."""

    auth_service = AuthService(db)
    try:
        payload = auth_service.decode_token(token)
        email = payload.get("sub")
        if not email:
            raise ValueError("Missing subject in token")
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
        ) from exc

    user = UserRepository(db).get_by_email(email)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
        )

    return user
