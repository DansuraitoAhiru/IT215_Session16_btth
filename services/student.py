from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from models.students import Student
from models.departments import Department
from models.enrollments import Enrollment
from models.courses import Course

def get_by_id(id: int, db: Session):
    student = db.query(Student).filter(Student.id == id).first()
    if not student:
        raise HTTPException (status.HTTP_404_NOT_FOUND, detail="Không tìm thấy sinh viên")
    departments = db.query(Department).filter(Department.id == student.department_id).all()
    enrollments = db.query(Enrollment).filter(Enrollment.student_id == id).all()
    course_ids = [e.course_id for e in enrollments]
    courses = db.query(Course).filter(Course.id.in_(course_ids)).all()
    return {
        "Sinh viên": student,
        "Phòng ban": departments,
        "Danh sách khóa học": courses
    }