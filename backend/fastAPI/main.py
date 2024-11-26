# Paso 1
# importar FastApi
# Iniciar servidor : uvicorn main:app --reload
from fastapi import FastAPI
from routers import users

# Crear la app
app = FastAPI()

# Routers
app.include_router(users.router)

#Paso 2
# Crear la ruta
@app.get("/")
async def root():
    return "Hola FastAPI!"

"""
# Crear rutas
@app.get("/ruta")
async def ruta():
    return {"ruta":"https://nombre/nombre"}
"""
