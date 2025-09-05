from fastapi_users import FastAPIUsers
from fastapi_users.authentication import JWTAuthentication
from models import User
from database import get_async_session
from fastapi_users import models

SECRET = "YOUR_SECRET_KEY"

fastapi_users = FastAPIUsers(
    get_async_session,
    [JWTAuthentication(secret=SECRET, lifetime_seconds=3600)],
    User,
    UserCreate,
    UserUpdate,
    UserDB
)
