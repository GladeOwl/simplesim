FROM python:3.11-slim-buster
RUN pip install 'uvicorn[standard]' 'fastapi'
WORKDIR /app
COPY . .
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "80"]