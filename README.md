# Servicio Telemático - API de Tareas

Este es un ejemplo básico de un servicio telemático construido con FastAPI y desplegado usando Docker.

## 📦 Requisitos
- Docker
- Git

## 🚀 Instrucciones de despliegue

1. Clona este repositorio:
```bash
git clone https://github.com/tu_usuario/servicio-api.git
cd servicio-api
```

2. Construye la imagen Docker:
```bash
docker build -t servicio-api .
```

3. Ejecuta el contenedor:
```bash
docker run -d -p 8000:8000 servicio-api
```

4. Accede al API en tu navegador o Postman:
- http://localhost:8000/docs → Documentación automática

## 🧪 Endpoints disponibles

- `GET /` → Saludo inicial
- `GET /tareas` → Lista de tareas
- `POST /tareas` → Crear una tarea (JSON)

## 🛠 Ejemplo de JSON para crear tarea
```json
{
  "id": 1,
  "titulo": "Estudiar para el examen",
  "descripcion": "Repasar contenido de AWS y contenedores"
}
```
