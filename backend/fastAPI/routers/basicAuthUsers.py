from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

router = APIRouter()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

class User(BaseModel):
    username: str
    fullName: str
    email: str
    disabled: bool


class UserDB(User):
    password: str
    
usersdb = {
    "stifle": {
        "username": "stifle",
        "fullName": "Adrian Belarte",
        "email": "adrian.belarte.it@gmail.com",
        "disabled": False,
        "password": "12345"
    },
    "zuleAnimalLove": {
        "username": "zuleAnimalLove",
        "fullName": "Zulema Gimenez",
        "email": "zulema.gimenez@gmail.com",
        "disabled": True,
        "password": "54321"
    }
}

def searchUserDB(username: str):
    if username in usersdb:
        return UserDB(**usersdb[username])
    
def searchUser(username: str):
    if username in usersdb:
        return User(**usersdb[username])

async def current_user(token: str = Depends(oauth2)):
    user = searchUser(token)
    if not user:
        raise HTTPException(
            status_code=401, 
            detail= "no authorizado", 
            headers={"WWW-Authenticate": "Bearer"}
        )
    
    if user.disabled:
        raise HTTPException(
            status_code= 400,
            detail="Usuario inactivo")
    
    return user

    
@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    userdb = usersdb.get(form.username)
    if not userdb:
        raise HTTPException(
            status_code=400, detail="Usuario no correcto")

    user =searchUserDB(form.username)
    if not form.password == user.password:
         raise HTTPException(
            status_code=400, detail="contrasenya no correcto")

    return {"access_token": user.username, "token_type": "bearer"}

@router.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user



            
