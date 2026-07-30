# syntax=docker/dockerfile:1

# ---------- Базовый слой: только прод-зависимости ----------
FROM python:3.13-slim AS base

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /app

# gettext — компиляция переводов ru/ky
# libjpeg/zlib — нужны Pillow для обработки фото проектов
RUN apt-get update && apt-get install -y --no-install-recommends \
        gettext \
        libjpeg62-turbo \
        zlib1g \
    && rm -rf /var/lib/apt/lists/*

# Зависимости копируем отдельно от кода: пока requirements.txt не менялся,
# Docker берёт этот слой из кэша и не переустанавливает пакеты при каждой правке
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /app

EXPOSE 8000

CMD ["gunicorn", "config.wsgi:application", \
     "--bind", "0.0.0.0:8000", \
     "--workers", "3", \
     "--timeout", "60", \
     "--access-logfile", "-", \
     "--error-logfile", "-"]

# ---------- Слой для разработки: + дев-инструменты, runserver вместо gunicorn ----------
FROM base AS dev

COPY requirements-dev.txt /app/
RUN pip install -r requirements-dev.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]