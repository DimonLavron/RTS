#!/bin/sh
source venv-site/bin/activate
exec gunicorn -b :5000 --access-logfile - --error-logfile - rts:app
