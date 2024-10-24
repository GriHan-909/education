from fastapi import FastAPI
from routers import task as r_t, user as r_u
from models import *


app = FastAPI()



@app.get('/')
async def welcome():
    return {"message": "Welcome to Taskmanager"}


app.include_router(r_t.router)
app.include_router(r_u.router)

