#!/bin/sh
source venv-rts/bin/activate
exec gunicorn -b :5000 rts:app