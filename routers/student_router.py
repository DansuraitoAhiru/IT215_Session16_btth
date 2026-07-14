from fastapi import APIRouter, Depends
from database import get_db
from sqlalchemy.orm import Session
from services.student import get_by_id

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)


@router.get("/{student_id}")
def get_students(student_id: int, db: Session=Depends(get_db)):
    return get_by_id(student_id, db)