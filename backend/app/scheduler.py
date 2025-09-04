from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from app.utils import send_email

scheduler = BackgroundScheduler()
scheduler.start()

def schedule_task(task):
    run_time = task.reminder_time
    if run_time > datetime.now():
        scheduler.add_job(
            func=send_email,
            trigger="date",
            run_date=run_time,
            args=[f"Reminder: {task.title}", f"Don't forget: {task.title}"],
            id=str(task.id),
            replace_existing=True
        )
        print(f"⏰ Task scheduled: {task.title} at {run_time}")
