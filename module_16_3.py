from fastapi import FastAPI, Path

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}



@app.get("/users")
async def ger_users() -> dict:
    return users

@app.post("/user/{username}/{age}")
async def add_users(username: str = Path(min_length=3, max_length=30, description='Enter your name', example='Alex'),
                    age: int = Path(ge=10, le=100, description='Enter your age', example=25)) -> str:
    current_index = str(int(max(users, key=int))+1)
    print(current_index, 'INDEX')
    users[current_index] = f'Имя: {username}, возраст: {age}'
    return f"User {current_index} is registered"

@app.put("/user/{user_id}/{username}/{age}")
async def update_message(user_id: str = Path(min_length=0, max_length=100, description='Enter your id', example="4"),
                         username: str = Path(min_length=3, max_length=30, description='Enter your name', example='Alex'),
                         age: int = Path(ge=10, le=100, description='Enter your age', example=25)) -> str:
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'User {user_id} has been updated'


@app.delete("/user/{user_id}")
async def info_user(user_id: str = Path(min_length=0, max_length=100, description='Enter id to delete', example="4")):
    users.pop(user_id)