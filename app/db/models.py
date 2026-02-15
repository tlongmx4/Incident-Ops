from sqlalchemy import Column, ForeignKey, Text, DateTime, Index, UniqueConstraint, CheckConstraint
from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy.sql import func
from datetime import datetime
from app.db.base import Base
from app.domains.enums import Severity, Status

class Incident(Base):
    __tablename__ = "incidents"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    public_id = Column(Text, nullable=False, unique=True)  # e.g., "INC-12345"
    title = Column(Text, nullable=False)
    description = Column(Text, nullable=True)
    status = Column(Text, nullable=False, default=Status.OPEN)
    severity = Column(Text, nullable=False, default=Severity.MEDIUM)
    service = Column(Text, nullable=True)  # e.g., "web", "database", "api"
    created_by_user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)  # User who created the incident
    incident_commander_user_id = Column(UUID(as_uuid=True),ForeignKey("users.id"), nullable=True)  # User responsible for managing the incident
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    started_at = Column(DateTime(timezone=True), nullable=True)
    mitigated_at = Column(DateTime(timezone=True), nullable=True)
    resolved_at = Column(DateTime(timezone=True), nullable=True)
    closed_at = Column(DateTime(timezone=True), nullable=True)

class IncidentResponder(Base):
    __tablename__ = "incident_responders"
    __table_args__ = (
        UniqueConstraint("incident_id", "user_id", name="uq_incident_user"),
        CheckConstraint("role IN ('responder', 'observer')", name="ck_incident_responders_role"),
    )

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    incident_id = Column(UUID(as_uuid=True), ForeignKey("incidents.id"), nullable=False, index=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False, index=True)
    role = Column(Text, nullable=False)  # e.g., "responder", "observer"
    assigned_at = Column(DateTime(timezone=True), server_default=func.now())

class IncidentUpdate(Base):
    __tablename__ = "incident_updates"
    __table_args__ = (
        Index("idx_incident_updates_incident_occurred", "incident_id", "occurred_at"),
        CheckConstraint("kind IN ('status_change', 'note', 'severity_change', 'action', 'comms', 'metric', 'assignment')", name="ck_incident_updates_kind"),
    )
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    incident_id = Column(UUID(as_uuid=True), ForeignKey("incidents.id"), nullable=False, index=True)
    kind = Column(Text, nullable=False)  # e.g., "status_change", "note", "assignment"
    message = Column(Text, nullable=True)
    author_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)  # User who made the update
    occurred_at = Column(DateTime(timezone=True), server_default=func.now(), index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(Text, nullable=False, unique=True)
    email = Column(Text, nullable=False, unique=True)
    full_name = Column(Text, nullable=True)
    role = Column(Text, nullable=False, default="user")  # e.g., "admin", "user"




