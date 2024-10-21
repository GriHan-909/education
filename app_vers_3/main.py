from fastapi import FastAPI
from routers import task as r_task, user as r_user
from models import *


app = FastAPI()



@app.get('/')
async def welcome():
    return {"message": "Welcome to Taskmanager"}


app.include_router(r_task.router)
app.include_router(r_user.router)

