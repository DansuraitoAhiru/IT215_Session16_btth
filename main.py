# Fleet – Driver là 1 - N
# Driver – Car là N - N, khóa ngoại (ForeignKey) dùng để liên kết Driver với Fleet đặt ở bảng Driver (fleet_id) vì quan hệ 1-N
# Quan hệ Nhiều - Nhiều giữa Driver và Car được SQLAlchemy ORM cấu hình gián tiếp qua bảng trung gian bookings

from fastapi import FastAPI
from database import Base, engine
from models import Fleet, Driver, Car, Booking

app = FastAPI()
Base.metadata.create_all(engine)
