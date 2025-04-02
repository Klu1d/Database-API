# FastAPI/PostgreSQL/SQLAlchemy
![image](https://github.com/user-attachments/assets/458b9303-7071-4c24-827e-366a789bab0e)

## Description
This is a local FastAPI-based application designed for managing data in PostgreSQL using SQLAlchemy. It provides a structured and efficient way to perform CRUD operations on various entities, such as companies, employees, cameras, and events.

## Technology Stack
- **FastAPI** - Web framework for building APIs
- **PostgreSQL** - Relational database management system
- **SQLAlchemy** - ORM for database interactions
- **AsyncPG** - Asynchronous PostgreSQL client

## Project Structure
```
.
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

## Installation
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
   - **DATABASE_URL** - The PostgreSQL connection URL (e.g., `postgresql+asyncpg://username:password@localhost/dbname`)
   Example `.env` file:
   ```
      DB_HOST=127.0.0.1
      DB_PORT=5432 # default PostgreSQL port
      DB_USER=
      DB_PASS=
      DB_NAME=
   ```

## Running the Application
Start the FastAPI server with:
```sh
uvicorn main:app --reload
```
The API documentation will be available at:
- **Swagger UI**: [http://127.0.0.1:8084/docs]
- **Redoc UI**: [http://127.0.0.1:8084/redoc]

## Available Endpoints
- **`POST /create/company`** - Create a new company
- **`GET /read/employee`** - Retrieve employee(s)
- **`PUT /update/employee`** - Update employee details
- **`DELETE /delete/company`** - Remove a company

More endpoints are available in the `routers` directory.
