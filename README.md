# Smart Task Management System

A Flask-based Smart Task Management System that supports user authentication, task CRUD operations, PostgreSQL integration, real-time updates using Flask-SocketIO, and analytics with Pandas and NumPy.

---

## Features

- User Registration, Login, and Logout
- Add, Update, Delete, and View Tasks
- PostgreSQL Database Integration with SQLAlchemy
- Task Analytics:
  - Total Tasks
  - Completed Tasks
  - Pending Tasks
  - Completion Percentage
- Real-Time Updates using Flask-SocketIO
- Responsive HTML/CSS Frontend

---

## Tech Stack

- Python
- Flask
- Flask-Login
- Flask-SQLAlchemy
- PostgreSQL
- Flask-SocketIO
- Pandas
- NumPy
- HTML, CSS, JavaScript

---

## Project Structure

```text
smart-task-manager/
├── analytics/
│   └── analytics.py
├── models/
│   └── models.py
├── routes/
│   ├── auth.py
│   └── tasks.py
├── static/
│   ├── css/
│   └── js/
├── templates/
├── app.py
├── config.py
├── requirements.txt
├── .env.example
└── README.md
```

---

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Aaradhya1998/task_manager.git
cd task_manager
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

**Windows**
```bash
venv\Scripts\activate
```

**macOS/Linux**
```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Create PostgreSQL Database

```sql
CREATE DATABASE task_manager;
```

### 6. Configure Environment Variables

Create a `.env` file:

```env
DATABASE_URL=postgresql://postgres:your_password@localhost:5432/task_manager
SECRET_KEY=your_secret_key_here
```

### 7. Run the Application

```bash
python app.py
```

Open in your browser:

```text
http://127.0.0.1:5000
```

---

## API Endpoints

### Authentication
- `GET/POST /register`
- `GET/POST /login`
- `GET /logout`

### Tasks
- `GET /tasks`
- `POST /tasks`
- `PUT /tasks/<id>`
- `DELETE /tasks/<id>`

---

## Analytics Example

```json
{
  "total_tasks": 10,
  "completed_tasks": 7,
  "pending_tasks": 3,
  "completion_percentage": 70.0
}
```

---

## Assignment Requirements Covered

- Python
- Flask
- REST API Development
- PostgreSQL Integration
- Pandas & NumPy
- WebSockets
- HTML/CSS Frontend

---

## Author

**Aaradhya Shekdar**

- GitHub: https://github.com/Aaradhya1998
- Portfolio: https://aaradhyashekdar.vercel.app/
- LinkedIn: https://www.linkedin.com/in/aaradhya-shekdar/

---

## License

This project was developed as part of a Python Development Internship assignment.
