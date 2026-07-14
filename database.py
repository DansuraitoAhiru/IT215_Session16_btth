from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DB_URL = "mysql+pymysql://root:WXvs6026%40@localhost:3306/student_db"
engine = create_engine(DB_URL)
Base = declarative_base()

SessionLocal = sessionmaker(
    autoflush=False,
    bind=engine,
    expire_on_commit=False
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()