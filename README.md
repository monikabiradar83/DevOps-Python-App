# DevOps Python App - CI/CD Pipeline using Jenkins and Docker

## Project Overview

This project demonstrates a complete CI/CD pipeline using Jenkins to automate the build and deployment of a Dockerized Flask application.

Whenever the source code is updated and pushed to GitHub, Jenkins pulls the latest code, builds a Docker image, removes the existing container, and deploys a new container automatically.

---

## Technologies Used

- Python
- Flask
- Git
- GitHub
- Docker
- Jenkins

---

## Project Structure

```
DevOps-Python-App
│
├── app.py
├── requirements.txt
├── Dockerfile
├── Jenkinsfile
└── README.md
```

---

## CI/CD Workflow

Developer
↓
GitHub Repository
↓
Jenkins Pipeline
↓
Build Docker Image
↓
Remove Old Container
↓
Run New Container
↓
Flask Application

---

## Jenkins Pipeline Stages

1. Checkout Source Code
2. Build Docker Image
3. Remove Existing Container
4. Deploy New Container

---

## Docker Commands Used

Build Image

docker build -t flask-app .

Run Container

docker run -d -p 5000:5000 --name flask-container flask-app

List Running Containers

docker ps

---

## Application URL

http://localhost:5000

---

## Learning Outcomes

- Jenkins Pipeline
- Docker Containerization
- Git & GitHub
- CI/CD Automation
- Flask Application Deployment

---

## Author

Monika Biradar