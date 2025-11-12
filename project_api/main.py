from fastapi import FastAPI, HTTPException, Body
from utils import read_data, write_data
from pydantic import BaseModel

app = FastAPI(title="Users API", version="1.0")



class User(BaseModel):
    name: str
    age: int

@app.post("/users")
def add_user(user: User):
    return {"msg": "User added!", "data": user}

@app.get("/users")
def get_users():
    return read_data()

@app.get("/users/{user_id}")
def get_user(user_id: int):
    dict_data=read_data()
    for data in dict_data:
        if data["id"]==user_id:
            return data
    raise HTTPException (status_code=404,detail="User not found")

# @app.post("/users")
# def add_user(data: dict = Body(...)):
#     arr_id=[]
#     list_data=read_data()
#     for data in list_data:
#         arr_id.append(data["id"])
#     try:
#         max_id=max(arr_id)+1
#     except:
#         max_id=1
#     new_user={"id":max_id,
#               "name":data.get("name"),
#               "age":data.get("age")}
#     if not new_user["name"] or not isinstance(new_user["age"], int):
#         raise HTTPException(status_code=400, detail="Invalid user data")

#     list_data.append(new_user)   
#     write_data(list_data)  
#     return new_user 
    