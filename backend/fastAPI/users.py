from fastapi import FastAPI
from pydantic import BaseModel
# Iniciar servidor : uvicorn users:app --reload

app = FastAPI()

# Entidad user
class User(BaseModel):
    id: int
    name: str
    surname: str
    age: int
    url: str

userslist = [User(id=1,name="Haydee", surname="Belarte",age=25,url="http://haydee.dev"),
         User(id=2,name="Adrian", surname="Belarte",age=35,url="http://adrian.dev"),
         User(id=3,name="David", surname="Peris",age=25,url="http://david.dev")]

@app.get("/usersjson")
async def usersjson():
    return [{"name": "Adrián", "surname": "Belarte","age": 34, "url": "http://adrian.dev"},
            {"name": "David", "surname": "Peris","age": 25, "url": "http://David.dev"}]

#Path
@app.get("/users/")
async def users():
    return userslist

@app.get("/user/{id}")
async def user(id: int):
    return searchUser(id)

# Query
@app.get("/user/")
async def user(id: int):
    return searchUser(id)

def searchUser(id: int):
    users = filter(lambda user: user.id == id, userslist)
    try:
        return list(users)[0]
    except:
        return "{no se ha encontrado el usuario}"

# Post
@app.post("/user/")
async def user(user: User):
    if type(searchUser(user.id)) == User:
        return "{Usuario ya existe}"
    else:
        userslist.append(user)
        return user

# Put
@app.put("/user/")
async def user(user: User):
    found = False
    for index, user in enumerate(userslist):
        if user.id == user.id:
            userslist[index] = user
            found = True
            
        
    if not found:
        return {"error: ""Usuario no actualizado"}
    else:
        return user

@app.delete("/user/{id}")
async def user(id:int):

    found = False

    for index, user in enumerate(userslist):
        if user.id == id:
            del userslist[index]
            found = True
            return {"Usuario eliminado con exito"}
        
    if not found:
      return {"error: ""Usuario no encontrado"}

        



