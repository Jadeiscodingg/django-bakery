# Bakery Django Application

## Setup Virtual Environment (venv)

1. Navigate to the project directory:

    ```bash
    cd bakery
    ```

2. Create a virtual environment:

    ```bash
    python -m venv newenv
    ```

3. Activate the virtual environment:

    On Windows:
    ```bash
    newenv\Scripts\activate
    ```

    On macOS/Linux:
    ```bash
    source newenv/bin/activate
    ```

4. Install dependencies from `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

5. Run the Django application:

    ```bash
    python manage.py runserver
    ```

## Running the Application with Docker

1. Build the Docker image:

    ```bash
    docker build -t bakery-django-app .
    ```

2. Run the Docker container:

    ```bash
    docker run -p 8000:8000 bakery-django-app
    ```

The application should now be accessible at `http://localhost:8000`.
