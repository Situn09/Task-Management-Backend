# Task-Management-Backend

A simple backend-only Task Management API built with **Flask**. Supports JWT authentication and task CRUD operations, deployed live via **Render**.

---

## 🚀 Live API

🌐 **Base URL:**  
https://task-management-backend-dak4.onrender.com

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
[Click to Open in Postman](https://situn09.postman.co/workspace/Team-Workspace~5f0a8861-df31-4b75-88fa-e1275f6754bf/collection/31754062-3509b871-3273-4df5-b56d-72b915cd530b?action=share&creator=31754062)

📥 Or import manually using `task-manager-api.postman_collection.json`.

---

## 🧑‍💻 How to Use Locally

```bash
# 1. Clone the repository
git clone https://github.com/Situn09/Task-Management-Backend.git
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

Great! Let’s deploy your Flask API to **Render**. Render is an awesome free/low-cost cloud platform that makes deploying backend APIs super simple.

---

## ✅ Deploy Flask API to Render

---

### 🧱 Project Structure

Make sure your folder structure looks like this:

```
task-api/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes/
│   │   ├── auth.py
│   │   └── tasks.py
│   └── utils.py
├── config.py
├── requirements.txt
├── run.py
├── .env (excluded from Git)
└── render.yaml ✅
```

### 5️⃣ Deploy to Render

1. Go to [https://render.com](https://render.com)
2. Click **"New +" → "Web Service"**
3. Connect your GitHub repo
4. Set:

   - **Environment**: Python
   - **Build Command**: _(leave blank)_
   - **Start Command**: `gunicorn run:app`
   - Add env vars:
     - `JWT_SECRET_KEY` → `your_secret_here`
     - `FLASK_ENV` → `production`
     - `DATABASE_URL` → `sqlite:///tasks.db` _(or a real DB if needed)_

5. Click **Deploy** 🚀

---

### ✅ After Deploying

You’ll get a public URL like:

```
https://task-api.onrender.com
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
