from database import Base
from sqlalchemy import String, Integer, Column, ForeignKey
from sqlalchemy.orm import relationship


class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(50), nullable=False)
    status = Column(String(20), nullable=False)
    enrollments = relationship("Enrollment", back_populates="course")