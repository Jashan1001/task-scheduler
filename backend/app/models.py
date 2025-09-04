from sqlalchemy import Column, Integer, String, DateTime
from app.database import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    email = Column(String, index=True)
    reminder_time = Column(DateTime, index=True)
    status = Column(String, default="pending")
