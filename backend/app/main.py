from fastapi import FastAPI, Depends
from app.core.config import settings
from datetime import datetime
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from sqlalchemy import text

app = FastAPI(title=settings.app_name)

@app.get("/")
async def home():
    return {"message":"Welcome to Job Tracker API"}

@app.get("/health")
async def health(db: Annotated[AsyncSession, Depends(get_db)]):
    await db.execute(text("SELECT 1"))
    return {"status":"ok", "database":"ok"}

@app.get("/about")
async def about():
    return {"app_name":"Job Tracker API", "Version":"1.0"}

#Used "Depends", "Dependancy Injection" & "Annoted" features for learning purpose
async def get_time():
    return datetime.now().strftime("%H:%M:%S")

@app.get("/showtime")
async def show_time(now: Annotated[str, Depends(get_time)]):
    return {"Current Time": now}

@app.get("/greetings")
async def greetings(now: Annotated[str, Depends(get_time)]):
    #return {"Message": f"Hello, Current time is {now}"}
    return {"Message": "Hello, Current time is {}".format(now)}