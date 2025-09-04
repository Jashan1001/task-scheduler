from pydantic import BaseModel
from datetime import datetime

class TaskBase(BaseModel):
    title: str
    email: str
    reminder_time: datetime

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int
    status: str

    class Config:
        from_attributes = True  # Updated for Pydantic V2
