#!/bin/bash
set -e

pip install -r requirements.txt
cd src
python manage.py collectstatic --noinput
python manage.py migrate
