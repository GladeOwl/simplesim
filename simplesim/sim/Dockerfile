FROM python:3.11-slim-buster
ARG years
ENV YEARS ${years} 
WORKDIR /app
COPY . .
CMD python /app/main.py ${YEARS}