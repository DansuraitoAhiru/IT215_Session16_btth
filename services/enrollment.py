from fastapi import HTTPException, status
from schemas.schemas import EnrollmentCreate
from sqlalchemy.orm import Session
from models.courses import Course
from models.departments import Department
from models.students import Student
from models.enrollments import Enrollment

def create_enrollment_service(enrollment: EnrollmentCreate, db: Session):
    student = db.query(Student).filter(Student.id == enrollment.student_id).first()
    if not student:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Không tìm thấy sinh viên")
    if student.status != "ACTIVE":
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "Trạng thái sinh viên đang không hoạt động")
    
    course = db.query(Course).filter(Course.id == enrollment.course_id).first()
    if not course:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Không tìm thấy khóa học")
    if course.status != "OPEN":
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "Khóa học đang không được mở")
    
    exist = db.query(Enrollment).filter(Enrollment.student_id == enrollment.student_id and Enrollment.course_id == enrollment.course_id)
    if exist:
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "Sinh viên đã đăng ký khóa học")
    
    new_enrollment = Enrollment(**enrollment.model_dump())
    db.add(new_enrollment)
    db.commit()
    db.refresh(new_enrollment)
    return {
        "message": "Tạo thành công đăng ký mới",
        "data": new_enrollment
    }