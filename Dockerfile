FROM python:3.14-slim

WORKDIR /app
COPY src/ ./src/

CMD ["python"]
