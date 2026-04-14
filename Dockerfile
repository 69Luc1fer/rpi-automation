# Використовуємо новішу базу Bullseye (Debian 11)
FROM python:3.9-slim-bullseye

# Встановлюємо робочу директорію
WORKDIR /app

# Встановлюємо залежності (тепер воно спрацює успішно)
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Встановлюємо бібліотеку для моніторингу
RUN pip install --no-cache-dir psutil

# Копіюємо код
COPY app.py .

# Запуск
CMD ["python", "app.py"]
