FROM python:3.12-slim

WORKDIR /app

COPY . /app

RUN pip install poetry && poetry install --no-root --only main

EXPOSE 8000

ENV PYTHONPATH=/app/app

CMD ["poetry", "run", "uvicorn", "main:main_app", "--host", "0.0.0.0", "--port", "8000"]