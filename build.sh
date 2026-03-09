#!/bin/bash
set -e

cd src
pip install -r ../requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate
