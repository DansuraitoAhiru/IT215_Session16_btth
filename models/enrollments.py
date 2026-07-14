from database import Base
from sqlalchemy import String, Integer, Column, ForeignKey
from sqlalchemy.orm import relationship


class Enrollment(Base):
    __tablename__ = "enrollments"
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    course_id = Column(Integer, ForeignKey("courses.id"))


    course = relationship("Course", back_populates="enrollments")
    student = relationship("Student", back_populates="enrollments")