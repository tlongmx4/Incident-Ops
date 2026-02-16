from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.db.session import get_db
from app.db.models import User
from app.schemas.users import UserCreate, UserRead

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def create_user(payload: UserCreate, db: Session = Depends(get_db)):
    """Create a new user."""
    user = User(
        username=payload.username,
        email=payload.email,
        full_name=payload.full_name,
        role=payload.role.value,
    )
    db.add(user)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Username or email already exists.")
    db.refresh(user)
    return user