FROM python:3.10.0

ENV PYTHONUNBUFFERED 1

WORKDIR /app
#
#COPY requirements.txt /code/requirements.txt
RUN pip install poetry

COPY . /app

RUN poetry install
WORKDIR /app/langstormapp
RUN poetry run python manage.py makemigrations
RUN poetry run python manage.py migrate

CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
