# Online Test Management System

## Overview
This project is an online test management system built using FastAPI and MySQL. It includes functionalities for user registration, test creation, question and answer management, and result retrieval.

## Prerequisites
- Python 3.x
- MySQL
- FastAPI
- SQLAlchemy
- Pytest

## Setup

1. **Clone the Repository**
    ```sh
    git clone <repository-url>
    cd <repository-folder>
    ```

2. **Create and Activate Virtual Environment**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install Dependencies**
    ```sh
    pip install -r requirements.txt
    ```

4. **Configure Database**
    - Ensure MySQL is running on your machine.
    - Create a database named `online_test_system`.
    - Update the database URL in `app/database.py` and `tests/conftest.py` if necessary.

5. **Run Migrations**
    ```sh
    alembic upgrade head
    ```

6. **Start the Application**
    ```sh
    uvicorn app.main:app --reload
    ```

## Running Tests

1. **Create Test Database**
    - Create a database named `online_test_system_test`.

2. **Run Tests**
    ```sh
    pytest
    ```

## Project Structure
