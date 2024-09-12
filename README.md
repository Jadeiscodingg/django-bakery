# Bakery Django Application

## Setup Virtual Environment (venv)
Things to take note of:
- Apply migrations using this command: `python manage.py makemigrations` or `python manage.py makemigrations shop`. Once you do that, apply `python manage.py migrate`. There should be no operational errors, and the app should open as expected.
- The `home.html` needed a change by line 6 of the for loop.

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

6. Check the `Screenshots` folder of the app.

## Docker Instructions

For users who prefer using Docker, follow these steps:

### Building the Docker Image

1. Ensure you are in the project root directory (where the `Dockerfile` is located).

2. Build the Docker image using:

    ```bash
    docker build -t jade399/django-app:v1 .
    ```

### Running the Docker Container

1. Run the Docker container with:

    ```bash
    docker run -p 8000:8000 jade399/django-app:v1
    ```

2. Open a browser and navigate to:

    ```
    http://localhost:8000
    ```

### Access the Django Admin

1. **Create a Superuser with my container id:**

    ```bash
    docker exec -it fe50045dba84 python manage.py createsuperuser
    ```

2. **Access the Admin Panel:**

    Navigate to:

    ```
    http://localhost:8000/admin
    ```

### Additional Docker Commands

- **Push the Docker Image to Docker Hub:**

    ```bash
    docker push jade399/django-app:v1
    ```

- **Pull the Docker Image:**

    ```bash
    docker pull jade399/django-app:v1
    ```





