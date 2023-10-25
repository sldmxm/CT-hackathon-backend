FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install -r /app/requirements.txt --no-cache-dir

COPY . .

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "backend.wsgi"]
