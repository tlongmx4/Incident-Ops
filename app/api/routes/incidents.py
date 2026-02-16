from uuid import UUID
import uuid
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.models import Incident
from app.db.session import get_db
from app.domains.enums import Status
from app.schemas.incidents import IncidentCreate, IncidentRead

router = APIRouter(prefix="/incidents", tags=["incidents"])

@router.post("/", response_model=IncidentRead, status_code=status.HTTP_201_CREATED)
def create_incident(payload: IncidentCreate, db: Session = Depends(get_db)):
    """Create a new incident."""
    incident = Incident(
        public_id=f"INC-{str(uuid.uuid4())[:8].upper()}",
        title=payload.title,
        description=payload.description,
        severity=payload.severity.value,
        service=payload.service,
        status=Status.OPEN,
        created_by_user_id=payload.created_by_user_id,
    )
    db.add(incident)
    db.commit()
    db.refresh(incident)
    return IncidentRead.model_validate(incident)



