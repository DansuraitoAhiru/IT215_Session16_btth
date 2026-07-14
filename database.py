from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine

URL_DB = "mysql+pymysql://root:WXvs6026%40@localhost:3306/fleet_db"

engine = create_engine(URL_DB)
LocalSession = sessionmaker(autoflush=False, autocommit=False, expire_on_commit=False, bind= engine)
Base = declarative_base()

def get_db():
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()
