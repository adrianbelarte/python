from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta
# uvicorn jwt_auth_users:app --reload

# Configuración
ALGORITHM = "HS256"
ACCESS_TOKEN_DURATION = 1
SECRET = "ewehlkehrmlnkdfhnbltr"

router = APIRouter()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")
crypt = CryptContext(schemes=["bcrypt"])

# Modelos
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
        "password": "$2a$12$jmCoAY2LrqjlkkmqQPIm0O/M9E/h6dCloft2NOjy8pKbptHtDji6a"
    },
    "zuleAnimalLove": {
        "username": "zuleAnimalLove",
        "fullName": "Zulema Gimenez",
        "email": "zulema.gimenez@gmail.com",
        "disabled": True,
        "password": "$2a$12$OrsWE2mzkTJu/Ab/CRV0qumCCKNxQBq6UNxpa2XGj0lOSYpPU6jKW"
    }
}

# Funciones auxiliares
def searchUserDB(username: str):
    user_data = usersdb.get(username)
    if user_data:
        return UserDB(**user_data)
    raise HTTPException(status_code=404, detail="Usuario no encontrado")

def search_user(username: str):
    if username in usersdb:
        return User(**usersdb[username])

# Rutas
@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    userdb = usersdb.get(form.username)
    if not userdb:
        raise HTTPException(status_code=400, detail="Usuario o contraseña incorrectos")

    user = searchUserDB(form.username)

    if not crypt.verify(form.password, user.password):
        raise HTTPException(status_code=400, detail="Usuario o contraseña incorrectos")

    access_token_expiration = timedelta(minutes=ACCESS_TOKEN_DURATION)
    expire = datetime.utcnow() + access_token_expiration
    access_token = {"sub": user.username, "exp": expire}

    return {
        "access_token": jwt.encode(access_token, SECRET, algorithm=ALGORITHM),
        "token_type": "bearer"
    }

async def current_user(user: User = Depends(oauth2)):
    if user.disabled:
        raise HTTPException(
            status_code=401, 
            detail= "no authorizado", 
            headers={"WWW-Authenticate": "Bearer"}
        )
    
    return user

async def auth_user(token: str = Depends(oauth2)):
    exception = HTTPException(
        status_code= 401,
            detail= "Credenciales inválidas",
            headers={"WWW-Authenticate", "Bearer"}
    )

    try:
        username = jwt.decode(token, SECRET, algorithms=[ALGORITHM]).get("sub")
        if username is None:
            raise exception
        
    except JWTError:
        raise exception
    
    return search_user(username)




@router.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user




