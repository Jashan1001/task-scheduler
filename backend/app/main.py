from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi_users import FastAPIUsers
from sqlalchemy.orm import Session
from crud import create_task, get_user_tasks, delete_task
from models import Task, User
from database import get_db
from users import fastapi_users

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include auth routes
app.include_router(fastapi_users.get_auth_router(JWTAuthentication(secret="YOUR_SECRET_KEY", lifetime_seconds=3600)), prefix="/auth/jwt", tags=["auth"])
app.include_router(fastapi_users.get_register_router(), prefix="/auth", tags=["auth"])

# Task endpoints
@app.post("/tasks/")
def create_task_endpoint(task: Task, user: User = Depends(fastapi_users.current_user())):
    db = next(get_db())
    return create_task(db, task, user.id)

@app.get("/tasks/")
def get_tasks_endpoint(user: User = Depends(fastapi_users.current_user())):
    db = next(get_db())
    return get_user_tasks(db, user.id)

@app.delete("/tasks/{task_id}")
def delete_task_endpoint(task_id: int, user: User = Depends(fastapi_users.current_user())):
    db = next(get_db())
    return delete_task(db, task_id, user.id)
