from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from typing import Literal


class Fleet(Base):
    __tablename__ = "fleets"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False) 
    driver = relationship("Driver", back_populates="fleet")


class Driver(Base):
    __tablename__ = "drivers"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    full_name = Column(String(100), nullable=False) 
    status = Column(String(20), default="ACTIVE", nullable=False)
    fleet_id = Column(Integer, ForeignKey("fleets.id"))
    fleet = relationship("Fleet", back_populates="driver")
    booking = relationship("Booking", back_populates="driver")
    cars = relationship("Car", secondary="bookings", back_populates="drivers")


class Car(Base):
    __tablename__ = "cars"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    license_plate  = Column(String(20), nullable=False) 
    status = Column(String(20), default="AVAILABLE", nullable=False)
    booking = relationship("Booking", back_populates="car")
    drivers = relationship("Driver", secondary="bookings", back_populates="cars")


class Booking(Base):
    __tablename__ = "bookings"
    id = Column(Integer, primary_key=True, autoincrement=True)
    driver_id = Column(Integer, ForeignKey("drivers.id"))
    car_id = Column(Integer, ForeignKey("cars.id"))
    driver = relationship("Driver", back_populates="bookings")
    car = relationship("Car", back_populates="bookings")
