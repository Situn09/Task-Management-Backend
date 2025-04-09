# Task-Management-Backend

A simple backend-only Task Management API built with **Flask**. Supports JWT authentication and task CRUD operations, deployed live via **Render**.

---

## 🚀 Live API

🌐 **Base URL:**  
https://task-api.onrender.com

---

## 📦 Features

- ✅ JWT-based authentication
- 🧑‍💻 User registration & login
- ✅ Task CRUD (Create, Read, Update, Delete)
- 🔐 Auth-protected endpoints
- ☁️ Hosted on Render
- 📬 Fully documented Postman collection

---

## 🧪 Test via Postman

👉 **Public Postman Collection:**  
[Click to Open in Postman](https://www.postman.com/your-username/workspace/task-manager/collection/abc123)

📥 Or import manually using `task-manager-api.postman_collection.json`.

---

## 🧑‍💻 How to Use Locally

```bash
# 1. Clone the repository
git clone https://github.com/your-username/flask-task-api.git
cd flask-task-api

# 2. Create virtual env and activate
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create a .env file and add:
echo "JWT_SECRET_KEY=your_secret_key" > .env

# 5. Run the app
python run.py
```

## 🔐 API Endpoints

### ✅ Auth

| Endpoint         | Method | Description         |
| ---------------- | ------ | ------------------- |
| `/auth/register` | POST   | Register user       |
| `/auth/login`    | POST   | Login and get token |

---

### ✅ Tasks (Require JWT)

All below routes require a header:

```
Authorization: Bearer <your_token>
```

| Endpoint           | Method | Description   |
| ------------------ | ------ | ------------- |
| `/tasks/`          | POST   | Create task   |
| `/tasks/`          | GET    | Get all tasks |
| `/tasks/<task_id>` | PUT    | Update a task |
| `/tasks/<task_id>` | DELETE | Delete a task |

---

## 💾 Example

### Register

```json
POST /auth/register
{
  "username": "john",
  "password": "secret123"
}
```

### Login

```json
POST /auth/login
{
  "username": "john",
  "password": "secret123"
}
```

Returns:

```json
{
  "access_token": "<JWT>"
}
```

Use this token in the header for task endpoints:

```
Authorization: Bearer <your_token>
```

---

## 🛠️ Tech Stack

- Python
- Flask
- Flask-JWT-Extended
- SQLite (can swap with PostgreSQL)
- Gunicorn
- Render (deployment)

---
