"""Authentication and authorization services."""
from datetime import datetime, timedelta, timezone

import jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from app.backend.config import get_settings
from app.backend.models.user_model import User
from app.backend.repositories.user_repository import UserRepository

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class AuthService:
    """Provides user authentication and JWT token issuance."""

    def __init__(self, db: Session) -> None:
        self.db = db
        self.user_repo = UserRepository(db)
        self.settings = get_settings()

    @staticmethod
    def hash_password(password: str) -> str:
        return pwd_context.hash(password)

    @staticmethod
    def verify_password(password: str, hashed_password: str) -> bool:
        return pwd_context.verify(password, hashed_password)

    def create_access_token(self, subject: str) -> str:
        expire = datetime.now(timezone.utc) + timedelta(
            minutes=self.settings.jwt_access_token_expire_minutes
        )
        payload = {"sub": subject, "exp": expire}
        return jwt.encode(
            payload,
            self.settings.jwt_secret_key,
            algorithm=self.settings.jwt_algorithm,
        )

    def register_user(self, email: str, full_name: str, password: str) -> User:
        existing_user = self.user_repo.get_by_email(email)
        if existing_user:
            raise ValueError("Email is already registered")

        user = User(
            email=email,
            full_name=full_name,
            hashed_password=self.hash_password(password),
        )
        return self.user_repo.create(user)

    def authenticate(self, email: str, password: str) -> User | None:
        user = self.user_repo.get_by_email(email)
        if not user:
            return None
        if not self.verify_password(password, user.hashed_password):
            return None
        return user

    def decode_token(self, token: str) -> dict:
        return jwt.decode(
            token,
            self.settings.jwt_secret_key,
            algorithms=[self.settings.jwt_algorithm],
        )
