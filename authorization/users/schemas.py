from datetime import datetime

from pydantic import BaseModel, EmailStr


class BaseUser(BaseModel):
    username: str
    first_name: str | None = None
    last_name: str | None = None
    email: EmailStr | None = None
    is_staff: bool = False
    is_active: bool = True
    created_at: datetime | None = None
    updated_at: datetime | None = None


class UserInDB(BaseUser):
    hashed_password: bytes
