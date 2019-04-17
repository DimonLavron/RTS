#!/bin/sh
source venv/bin/activate
exec gunicorn -b :8000 app:app
