from fastapi import FastAPI
from routers import users  # Importa el router desde users.py
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

@app.get("/health")
async def health_check():
    return {"status": "ok"}

