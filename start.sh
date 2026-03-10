#!/bin/sh
cd src
exec gunicorn myproject.wsgi --bind "0.0.0.0:${PORT}" --workers 2 --timeout 120
