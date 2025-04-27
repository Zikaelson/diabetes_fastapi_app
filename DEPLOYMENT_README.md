# 🚀 Deploying a FastAPI + Streamlit App to AWS EC2 using GitHub Actions CI/CD + Docker Hub

This README covers **everything** needed to:
- Build and containerize a FastAPI backend and Streamlit frontend
- Push images to Docker Hub
- Deploy automatically to AWS EC2 using GitHub Actions (CI/CD pipeline)

# 📋 1. Project Structure
```bash
diabetes-fastapi-app/
│
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── .github/workflows/
│   └── deploy.yml
│
└── README.md
```

# 🛠️ 2. Technologies Used
| Tool | Purpose |
|:---|:---|
| FastAPI | Backend server (Python) |
| Streamlit | Frontend UI (Python) |
| Docker | Containerization |
| Docker Hub | Image hosting |
| AWS EC2 | Cloud server |
| GitHub Actions | CI/CD pipeline |

# ⚙️ 3. Step-by-Step Setup Guide
## 3.1 Backend (FastAPI)
(Dockerfile and code setup steps)

## 3.2 Frontend (Streamlit)
(Dockerfile and code setup steps)

# 🛳️ 4. Docker Hub
(Create account, create repositories, login locally)

# ☁️ 5. AWS EC2 Setup
(Launch EC2 instance, security group setup, download .pem key, username: ec2-user)

# 🔥 6. GitHub Actions CI/CD Setup
(Add GitHub Secrets for Docker and EC2 credentials)

# 🛠️ 7. Final deploy.yml
(Full deploy.yml content)

# 🧹 8. Issues I Faced and How I Solved Them
(SSH auth issues, port conflicts, docker kill missing containers)

# 🚀 9. How Deployment Works Now
(Automated deployment on git push)

# 🔥 10. Health Check Commands
(ssh, docker ps, docker logs)

# ✨ 11. Conclusion
(You now have a fully working CI/CD setup)

# 📌 Final Note
If you get stuck:
- Check `.pem` key
- Check Docker login
- Check EC2 security group rules (port 22, 8000, 8501)
- Check GitHub Secrets spelling
- Restart EC2 server clean if needed

**You can always fix it! 🚀**