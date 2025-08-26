#!/bin/sh

set -e

echo "👉 Собираем статику..."
poetry run python manage.py collectstatic --noinput

echo "📦 Применяем миграции..."
poetry run python manage.py migrate

echo "🚀 Запускаем Gunicorn..."
poetry run gunicorn config.wsgi:application --bind 0.0.0.0:8000