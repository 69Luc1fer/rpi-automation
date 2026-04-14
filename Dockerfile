FROM python:3.9-slim-buster
WORKDIR /app
# Встановлюємо залежності для psutil
RUN apt-get update && apt-get install -y gcc python3-dev && rm -rf /var/lib/apt/lists/*
RUN pip install psutil
COPY app.py .
CMD ["python", "app.py"]
