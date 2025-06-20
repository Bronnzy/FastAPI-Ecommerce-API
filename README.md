# FastAPI-Ecommerce-API

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/aliseyedi01/Ecommerce-Api.git
   ```

2. **Navigate to the project directory:**

   ```bash
   FastAPI-Ecommerce-API
   ```

3. **Create a virtual environment:**

   ```bash
   python3 -m venv venv
   ```

4. **Activate the virtual environment:**

   On Windows:

   ```bash
   venv\Scripts\activate
   ```

   On macOS and Linux:

   ```bash
   source venv/bin/activate
   ```

5. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run Alembic migrations:**

   ```bash
   python migrate.py
   ```

   This will apply any pending database migrations.

2. **Run the FastAPI development server:**

   ```bash
   uvicorn main:app --host localhost --port 8000 --reload
   ```

   The API will be accessible at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

3. **Access the Swagger UI and ReDoc:**

   - Swagger UI: [http://127.0.0.1:8000/docs/](http://127.0.0.1:8000/docs/)
   - ReDoc: [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)
