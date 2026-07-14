from database import Base
from sqlalchemy import String, Integer, Column
from sqlalchemy.orm import relationship


class Department(Base):
    __tablename__ = "departments"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    students = relationship("Student", back_populates="department")