from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List
from uuid import UUID
from app.domains.enums import Severity, Status

class IncidentCreate(BaseModel):
    title: str
    description: Optional[str] = None
    severity: Severity = Severity.MEDIUM
    service: Optional[str] = None
    created_by_user_id: UUID

class IncidentRead(BaseModel):
    id: UUID
    public_id: str
    title: str
    description: Optional[str] = None
    status: Status
    severity: Severity
    service: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}
 