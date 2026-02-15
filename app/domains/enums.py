from enum import StrEnum

class Status(StrEnum):
        OPEN = "open"
        INVESTIGATING = "investigating"
        MITIGATED = "mitigated"
        RESOLVED = "resolved"
        CLOSED = "closed"

class Severity(StrEnum):
        LOW = "low"
        MEDIUM = "medium"
        HIGH = "high"
        CRITICAL = "critical"

class UpdateKind(StrEnum):
        STATUS_CHANGE = "status_change"
        NOTE = "note"
        SEVERITY_CHANGE = "severity_change"
        ACTION = "action"
        COMMS = "comms"
        METRIC = "metric"
        ASSIGNMENT = "assignment"

class UserRole(StrEnum):
        ADMIN = "admin"
        USER = "user"
        OBSERVER = "observer"
        RESPONDER = "responder"
        