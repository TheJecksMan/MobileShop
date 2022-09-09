FROM python:3.10-slim

EXPOSE 80

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
COPY ./app /app

#CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
CMD ["gunicorn", "--bind", "0.0.0.0:80", "-k", "uvicorn.workers.UvicornWorker", "main:app"]
