# Department – Student là 1-N
# Student – Course là N-N
# Khóa ngoại liên kết sinh viên với phòng ban đặt trong bảng students
# Quan hệ giữa sinh viên và khóa học cần danh sách trung gian enrollments


from fastapi import FastAPI, Depends, HTTPException, status
from database import Base, engine, get_db
from routers.student_router import router as student_router
from routers.enrollment_rounter import router as enrollment_router
from sqlalchemy.orm import Session
from sqlalchemy import text
from models import courses, students, enrollments, departments

Base.metadata.create_all(engine)

app = FastAPI()
app.include_router(student_router)
app.include_router(enrollment_router)

@app.get("/test-connection")
def test_db_connection(db: Session = Depends(get_db)):
    try:
        db.execute(text('SELECT 1'))
        return {
            "status": "Success",
            "message": "Kết nối thành công"
        }
    except Exception as error:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, str(error))