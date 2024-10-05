from fastapi import FastAPI, Path, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

users = []

class User(BaseModel):
    id: int
    username: str
    age: int

@app.get("/users")
async def ger_users() -> List[User]:
    return users

@app.post("/user/{username}/{age}", response_model=User)
async def add_users(username: str = Path(min_length=3, max_length=30, description='Enter name', example='Alex'),
                    age: int = Path(ge=10, le=100, description='Enter age', example=25)) -> User:
    current_index = 1 if not users else max(user.id for user in users) + 1
    new_user = User(id=current_index, username=username, age=age)
    users.append(new_user)
    return new_user

@app.put("/user/{user_id}/{username}/{age}")
async def update_message(user_id: int = Path(ge=0, le=100, description='Enter id', example=4),
                         username: str = Path(min_length=3, max_length=30, description='Enter name', example='Alex'),
                         age: int = Path(ge=10, le=100, description='Enter age', example=25)) -> User:
    try:
        edit_user = users[user_id-1]
        edit_user.username = username
        edit_user.age = age
        return users[user_id-1]
    except IndexError:
        raise HTTPException(status_code=404, detail='User was not found')


@app.delete("/user/{user_id}")
async def info_user(user_id: int = Path(ge=0, le=100, description='Enter id to delete', example=4)):
    try:
        return users.pop(user_id-1)
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")