from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from fastapi_users.db import SQLAlchemyBaseUserTable
from database import Base

class User(SQLAlchemyBaseUserTable, Base):
    pass

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    scheduled_time = Column(DateTime)
    owner_id = Column(Integer, ForeignKey("user.id"))
    
    owner = relationship("User")
