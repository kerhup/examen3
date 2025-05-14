from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Datos en memoria para simular una base de datos
tareas = []

class Tarea(BaseModel):
    id: int
    titulo: str
    descripcion: str

@app.get("/")
def root():
    return {"mensaje": "API de tareas activa"}

@app.get("/tareas")
def listar_tareas():
    return tareas

@app.post("/tareas")
def crear_tarea(tarea: Tarea):
    tareas.append(tarea)
    return {"mensaje": "Tarea creada", "tarea": tarea}
