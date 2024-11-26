from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

# Crear el router
router = APIRouter(
    prefix="/users",  # Prefijo para todas las rutas
    tags=["users"],  # Categoría para la documentación
    responses={404: {"message": "No encontrado"}}
)

# Modelo de usuario
class User(BaseModel):
    id: int
    name: str
    surname: str
    age: int
    url: str

# Lista de usuarios inicial
users_list = [
    User(id=1, name="Haydee", surname="Belarte", age=25, url="http://haydee.dev"),
    User(id=2, name="Adrian", surname="Belarte", age=35, url="http://adrian.dev"),
    User(id=3, name="David", surname="Peris", age=25, url="http://david.dev"),
]

# Rutas

# Obtener todos los usuarios
@router.get("/", response_model=List[User])
async def get_users():
    return users_list

# Obtener un usuario por ID (Path Parameter)
@router.get("/{id}", response_model=User)
async def get_user(id: int):
    user = search_user(id)
    if user:
        return user
    return {"error": "Usuario no encontrado"}

# Obtener un usuario por ID (Query Parameter)
@router.get("/search/", response_model=User)
async def get_user_by_query(id: int):
    user = search_user(id)
    if user:
        return user
    return {"error": "Usuario no encontrado"}

# Crear un nuevo usuario
@router.post("/", response_model=User)
async def create_user(user: User):
    if search_user(user.id):
        return {"error": "El usuario ya existe"}
    users_list.append(user)
    return user

# Actualizar un usuario
@router.put("/", response_model=User)
async def update_user(user: User):
    for index, existing_user in enumerate(users_list):
        if existing_user.id == user.id:
            users_list[index] = user
            return user
    return {"error": "Usuario no encontrado"}

# Eliminar un usuario
@router.delete("/{id}")
async def delete_user(id: int):
    for index, user in enumerate(users_list):
        if user.id == id:
            del users_list[index]
            return {"message": "Usuario eliminado con éxito"}
    return {"error": "Usuario no encontrado"}

# Función auxiliar para buscar usuarios
def search_user(id: int):
    return next((user for user in users_list if user.id == id), None)

        



