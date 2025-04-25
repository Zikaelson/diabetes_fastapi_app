# 📘 README2: End-to-End Deployment with FastAPI + Streamlit + Docker

This is a fully containerized data science project that includes:

- 🔬 A machine learning backend (FastAPI + scikit-learn)
- 🎛️ A frontend UI (Streamlit)
- 🐳 Containerized using Docker
- 🔁 Orchestrated with `docker-compose`
- ☁️ Backend and frontend images pushed to Docker Hub

---

## 📁 Folder Structure

```
DIABETES_FASTAPI_APP/
├── backend/
│   ├── main.py
│   ├── model.pkl
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
├── docker-compose.yml
├── README2.md
```

---

## 🚀 Step-by-Step Setup

### ✅ Prerequisites

- Python (locally, for testing)
- Docker Desktop installed
- Docker Hub account (free, no card needed)

---

## 🧠 Backend (FastAPI) Setup

### 1. Navigate to backend

```bash
cd DIABETES_FASTAPI_APP/backend
```

### 2. Create `Dockerfile`

```
FROM python:3.11-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### 3. Build Docker Image

```bash
docker build -t fastapi-diabetes-backend .
```

### 4. Tag for Docker Hub

```bash
docker tag fastapi-diabetes-backend zikaelson/fastapi-diabetes-backend:latest
```

### 5. Push to Docker Hub

```bash
docker push zikaelson/fastapi-diabetes-backend:latest
```

---

## 🖼️ Frontend (Streamlit) Setup

### 1. Navigate to frontend

```bash
cd ../frontend
```

### 2. Create `Dockerfile`

```
FROM python:3.11-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

### 3. Build Docker Image

```bash
docker build -t diabetes-streamlit-frontend .
```

### 4. Tag for Docker Hub

```bash
docker tag diabetes-streamlit-frontend zikaelson/diabetes-streamlit-frontend:latest
```

### 5. Push to Docker Hub

```bash
docker push zikaelson/diabetes-streamlit-frontend:latest
```

---

## 🧩 Compose It All Together

### 1. Go to root folder

```bash
cd ..
```

### 2. Create `docker-compose.yml`

```
services:
  backend:
    image: zikaelson/fastapi-diabetes-backend:latest
    ports:
      - "8000:8000"

  frontend:
    image: zikaelson/diabetes-streamlit-frontend:latest
    ports:
      - "8501:8501"
    depends_on:
      - backend
```

### 3. Run both together:

```bash
docker-compose up
```

---

## ⚠️ Troubleshooting

### ❌ Error: Port Already in Use

```bash
Bind for 0.0.0.0:8000 failed: port is already allocated
```

✅ Fix:

```bash
netstat -ano | findstr :8000
taskkill /PID <pid> /F
```

### ❌ Docker not recognized

✅ Fix: Open Docker Desktop manually and wait for it to start.

### ❌ WSL update failed

✅ Fix:

```bash
wsl --update
```

Or install WSL manually: https://aka.ms/wsl2

---

## 🧼 Shut Down Cleanly

```bash
docker-compose down
```

---

## 🧽 Optional Cleanup

```bash
docker system prune -a
```

---

## 🔧 All Essential Docker Commands

| Description | Command |
|------------|---------|
| Build image | `docker build -t name .` |
| List images | `docker images` |
| Remove image | `docker rmi image_id` |
| Run container | `docker run -p 8000:8000 name` |
| List containers | `docker ps -a` |
| Stop container | `docker stop container_id` |
| Remove container | `docker rm container_id` |
| Compose up | `docker-compose up` |
| Compose down | `docker-compose down` |
| View logs | `docker-compose logs` |
| Clean up all | `docker system prune -a` |

---

## ✅ Final Notes

- All backend and frontend components are containerized
- Docker Compose launches everything in sync
- Project is fully portable and cloud-ready
- Use this README2 as your bible for replication

---

**Built by Zikaelson | 2025 🐳**