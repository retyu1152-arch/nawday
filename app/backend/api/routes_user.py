"""User and authentication API routes."""
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.backend.api.deps import get_current_user
from app.backend.models.base import get_db
from app.backend.models.user_model import User
from app.backend.schemas.user_schema import Token, UserCreate, UserRead
from app.backend.services.auth_service import AuthService

router = APIRouter(prefix="/api/users", tags=["users"])


@router.post("/register", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def register_user(payload: UserCreate, db: Session = Depends(get_db)) -> User:
    """Register a new user account."""

    auth_service = AuthService(db)
    try:
        return auth_service.register_user(
            email=payload.email,
            full_name=payload.full_name,
            password=payload.password,
        )
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@router.post("/login", response_model=Token)
def login_user(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
) -> Token:
    """Authenticate user and return JWT token."""

    auth_service = AuthService(db)
    user = auth_service.authenticate(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
        )
    token = auth_service.create_access_token(subject=user.email)
    return Token(access_token=token)


@router.get("/me", response_model=UserRead)
def read_current_user(current_user: User = Depends(get_current_user)) -> User:
    """Get current authenticated user profile."""

    return current_user
