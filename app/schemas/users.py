from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from app.domains.enums import UserRole

class UserCreate(BaseModel):
    username: str
    email: str
    full_name: Optional[str] = None
    role: UserRole = UserRole.USER

class UserRead(BaseModel):
    id: UUID
    username: str
    email: str
    full_name: Optional[str] = None
    role: UserRole

    model_config = {"from_attributes": True}