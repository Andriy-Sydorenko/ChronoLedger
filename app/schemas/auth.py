from pydantic import BaseModel, EmailStr, Field, SecretStr

from app.schemas.base import BaseValidatedModel


class UserRegister(BaseValidatedModel):
    email: str = EmailStr()
    password: SecretStr = Field(..., min_length=8)
    username: str | None = Field(None, min_length=3)


class UserRegisterResponse(BaseModel):
    email: str = EmailStr()
    username: str | None = Field(None, min_length=3)

    class Config:
        from_attributes = True


class UserLogin(BaseValidatedModel):
    email: str = EmailStr()
    password: SecretStr = Field(..., min_length=8)


class UserLoginResponse(BaseModel):
    token: str
    token_type: str = "bearer"
