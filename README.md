# Bakery Django Application

## Setup Virtual Environment (venv)
Things to take note of:
- apply migrations using this command : python manage.py makemigrations or python manage.py makemigrations shop
  Once you do that apply python manage.py migrate, there will be no operational errors an the pp should open as expected.

- The home.html needed a change by line 6 of the for loop.

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

Check Screenshots folder of the app



