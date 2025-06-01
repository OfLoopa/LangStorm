# Install requirements

Needs Python >=3.10

Run following commands:
```
pip install poetry
poetry install
```

# Run

To run - database must be set up (self-hosted or in Docker)
Credits for database stored in `langstormapp/settigns.py`

First step is to run database migrations:
`poetry run python manage.py migrate`

To run server:
`poetry run python manage.py runserver 0.0.0.0:8000`
