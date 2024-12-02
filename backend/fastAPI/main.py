from fastapi import FastAPI
from routers import users, basicAuthUsers, jwt_auth_users  # Importa el router desde users.py
from fastapi.staticfiles import StaticFiles #Importar static files

# uvicorn main:app --reload
# Crear la app
app = FastAPI(
    title="Mi API",
    description="Descripción de mi API",
    version="1.0.0",
    docs_url="/"  # Mueve Swagger UI a la raíz
)


# Incluir el router de users
app.include_router(users.router)
app.include_router(basicAuthUsers.router)
app.include_router(jwt_auth_users.router)
# Para llamar a un recurso statico
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/health")
async def health_check():
    return {"status": "ok"}

