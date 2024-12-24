# Используем официальный образ Python
FROM python:3.9-slim
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PWDEBUG=1
ENV APP_POSTGRES_HOST=localhost
ENV APP_POSTGRES_PORT=5432
ENV APP_PROTOKOL=http
ENV APP_POSTGRES_PASS=123
ENV APP_POSTGRES_LOGIN=postgres
ENV APP_POSTGRES_DBNAME=library
ENV SECRET_KEY=562778be-3e23-407e-8544-f5bc184cb547
# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы зависимостей
COPY requirements.txt requirements.txt

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы приложения
COPY . .

# Указываем переменную окружения для Flask
ENV FLASK_APP=app.py

# Открываем порт для приложения
EXPOSE 5000

# Команда для запуска приложения
CMD ["flask", "run", "--host=0.0.0.0"]