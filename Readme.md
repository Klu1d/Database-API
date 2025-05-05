# FastAPI/PostgreSQL/SQLAlchemy
![image](https://github.com/user-attachments/assets/55571b8d-b770-4a5b-aa83-84e705827fa0)

## 📦 Description
This is a local FastAPI-based application designed for managing data in PostgreSQL using SQLAlchemy. It provides a structured and efficient way to perform CRUD operations on various entities, such as companies, employees, cameras, and events.

## 🛠 Technology Stack
- **FastAPI** - Web framework for building APIs
- **PostgreSQL** - Relational database management system
- **SQLAlchemy** - ORM for database interactions
- **AsyncPG** - Asynchronous PostgreSQL client

## 🧱 Project Structure
```
.
├── auth.py          # Authentication
├── crud.py          # Database interaction logic
├── database.py      # Database connection setup
├── main.py          # FastAPI entry point
├── models/          # Pydantic models
│   ├── company.py
│   ├── employee.py
│   ├── camera.py
│   ├── event.py
├── routers/         # API endpoints
│   ├── create.py
│   ├── read.py
│   ├── update.py
│   ├── delete.py
├── schemas/         # Database schemas
│   ├── companies.py
│   ├── employees.py
│   ├── cameras.py
│   ├── events.py
├── requirements.txt # Required dependencies
```

## 🛠 Installation

### 🔧 Option 1: Manual Setup

1. Clone the repository:
   ```sh
   git clone https://github.com/Klu1d/Database-API.git
   cd Database-API/app
   ```

2. Create a virtual environment:
   ```sh
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Set up the PostgreSQL database and configure the connection in the `.env` file:

   Example `.env` file:
   ```
   API_KEY=your_generated_key_here

   DB_HOST=127.0.0.1
   DB_PORT=5432
   DB_USER=your_user
   DB_PASS=your_password
   DB_NAME=your_db_name
   ```

---

### 🐳 Option 2: Run with Docker

> **Note**: Requires Docker and Docker Compose installed.

1. Clone the repository:
   ```sh
   git clone https://github.com/Klu1d/Database-API.git
   cd Database-API
   ```

2. Create a `.env` file in the root of the project (same folder as `docker-compose.yml`):

   ```
   API_KEY=your_generated_key_here
   ```

3. Run the containers:
   ```sh
   docker-compose up --build
   ```

4. The API will be available at:
   ```
   http://localhost:8089/docs
   ```

## 🚀 Running the Application
Start the FastAPI server with:
```sh
uvicorn main:app --reload
```
The API documentation will be available at:
- **Swagger UI**: [http://127.0.0.1:8084/docs]
- **Redoc UI**: [http://127.0.0.1:8084/redoc]
