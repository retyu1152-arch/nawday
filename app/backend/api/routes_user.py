from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.backend.repositories.user_repository import UserRepository
from app.backend.schemas.user_schema import Token, UserCreate, UserLogin, UserRead
from app.backend.utils.db import get_db
from app.backend.utils.security import create_access_token, hash_password, verify_password

router = APIRouter(prefix="/api/users", tags=["users"])


@router.post("/register", response_model=UserRead)
def register(payload: UserCreate, db: Session = Depends(get_db)):
    repo = UserRepository(db)
    if repo.get_by_email(payload.email):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Email already registered")
    return repo.create(email=payload.email, hashed_password=hash_password(payload.password))


@router.post("/login", response_model=Token)
def login(payload: UserLogin, db: Session = Depends(get_db)):
    repo = UserRepository(db)
    user = repo.get_by_email(payload.email)
    if not user or not verify_password(payload.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    return Token(access_token=create_access_token(user.email))
