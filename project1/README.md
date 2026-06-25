
---

### 📄 `project1/README.md`


# Project 1: Flask App with Docker

This project demonstrates how to run a simple Flask application inside a Docker container.

## 📦 Project Structure
```markdown
project1/
├── Dockerfile
├── flask-app.py
├── requirements.txt
├── README.md
└── venv/ (ignored in Git)
```

## 🚀 Running Locally

1. Create a virtual environment (optional):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
  
2.Run the Flask app:
  ```bash
  python flask-app.py
  ```

## 🐳 Running with Docker

1.Build the Docker image:
  ```bash
  docker build -t flask-app .
 ```
2.Run the container:
  ```bash
 docker run -p 5000:5000 flask-app
 ```
3.Open your browser at:
  ```bash
  http://localhost:5000
  ```
## 🖼 Output
<img width="1533" height="768" alt="Screenshot 2026-06-25 122606" src="https://github.com/user-attachments/assets/fbfaa722-5f42-42ef-aa13-71dc8da6fae0" />
