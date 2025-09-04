from fastapi import FastAPI, HTTPException
from app import models, schemas, crud, database, scheduler
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

# Create database tables
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Task Scheduler API")

# Allow frontend access (if added later)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/tasks/", response_model=schemas.Task)
def create_task(task: schemas.TaskCreate):
    db: Session = database.SessionLocal()
    db_task = crud.create_task(db, task)
    scheduler.schedule_task(db_task)  # Schedule email reminder
    return db_task

@app.get("/tasks/", response_model=list[schemas.Task])
def read_tasks(skip: int = 0, limit: int = 100):
    db: Session = database.SessionLocal()
    return crud.get_tasks(db, skip=skip, limit=limit)

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    db: Session = database.SessionLocal()
    deleted = crud.delete_task(db, task_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted"}
