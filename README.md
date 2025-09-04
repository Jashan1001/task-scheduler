# Automated Task Scheduler

## Overview
A Python-based task scheduler that sends email reminders for tasks.  
Backend is built with **FastAPI**, using **APScheduler** for scheduling, and emails are sent via **Gmail SMTP**.

Frontend (React dashboard) and cloud deployment (AWS Lambda) will be added later.

---

## Features
- Create and manage tasks
- Schedule email reminders
- Serverless-ready architecture

---

## Tech Stack
- Python, FastAPI, APScheduler
- Gmail SMTP for email
- SQLite (local DB; will migrate to cloud DB later)

---

### Notes
- Keep `.env` private and do not push to GitHub.
- APScheduler runs tasks in the background and triggers emails at scheduled times.
