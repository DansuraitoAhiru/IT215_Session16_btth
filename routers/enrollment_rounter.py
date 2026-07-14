from fastapi import APIRouter, Depends
from database import get_db
from sqlalchemy.orm import Session
from services.enrollment import create_enrollment_service
from schemas.schemas import EnrollmentCreate

router = APIRouter(
    prefix="/enrollmets",
    tags=["Enrollments"]
)


@router.post("", status_code=201)
def create_enrollment(enrollment: EnrollmentCreate, db: Session = Depends(get_db)):
    return create_enrollment_service(enrollment, db)