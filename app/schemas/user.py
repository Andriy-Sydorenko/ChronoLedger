from pydantic import BaseModel, EmailStr, HttpUrl, SecretStr

from app.schemas.base import BaseValidatedModel


class UserUpdate(BaseValidatedModel):
    username: str | None = None
    password: SecretStr | None = None


class UserUpdateResponse(BaseModel):
    email: EmailStr
    username: str | None = None
    avatar_url: HttpUrl | None

    class Config:
        from_attributes = True
