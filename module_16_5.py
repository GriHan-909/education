from fastapi import FastAPI, Path, HTTPException, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List
from fastapi.templating import Jinja2Templates


app = FastAPI()
templates = Jinja2Templates(directory='templates')

class User(BaseModel):
    id: int
    username: str
    age: int


users_db: List[User] = []

@app.get('/')
async def get_all_messages(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "users": users_db})



@app.get("/users/{user_id}")
async def ger_users(request: Request, user_id: int) -> HTMLResponse:
    try:
        return templates.TemplateResponse("users.html", {"request": request, "user": users_db[user_id - 1]})
    except IndexError:
        raise HTTPException(status_code=404, detail='User not found')


@app.post("/user/{username}/{age}", response_model=User)
async def add_users(username: str = Path(min_length=3, max_length=30, description='Enter name', example='Alex'),
                    age: int = Path(ge=10, le=100, description='Enter age', example=25)) -> User:
    current_index = 1 if not users_db else max(user.id for user in users_db) + 1
    new_user = User(id=current_index, username=username, age=age)
    users_db.append(new_user)
    return new_user

@app.put("/user/{user_id}/{username}/{age}")
async def update_message(user_id: int = Path(ge=0, le=100, description='Enter id', example=4),
                         username: str = Path(min_length=3, max_length=30, description='Enter name', example='Alex'),
                         age: int = Path(ge=10, le=100, description='Enter age', example=25)) -> User:
    try:
        edit_user = users_db[user_id-1]
        edit_user.username = username
        edit_user.age = age
        return users_db[user_id-1]
    except IndexError:
        raise HTTPException(status_code=404, detail='User was not found')


@app.delete("/user/{user_id}")
async def info_user(user_id: int = Path(ge=0, le=100, description='Enter id to delete', example=4)):
    try:
        return users_db.pop(user_id-1)
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")