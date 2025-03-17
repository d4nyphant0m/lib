# Django Project: Lib

A Django application skeleton.

## Setup

1. Clone the repository
```bash
git clone https://github.com/d4nyphant0m/lib.git
cd lib
```

2. Create a virtual environment and activate it
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run migrations
```bash
python manage.py migrate
```

5. Create a superuser
```bash
python manage.py createsuperuser
```

6. Run the development server
```bash
python manage.py runserver
```

## Project Structure

- `config/`: Main Django project settings
- `core/`: Main Django application with common functionality

## Development

- To create a new app: `python manage.py startapp app_name`
- To run tests: `python manage.py test`
- To generate migrations: `python manage.py makemigrations`