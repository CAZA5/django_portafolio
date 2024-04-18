#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
pip install -r requirements.txt

# Convert static asset files
pip freeze > requirements.txt
python manage.py collectstatic --no-input
pip install -r requirements.txt
# Apply any outstanding database migrations
#install gunicorn
pipenv install gunicorn
gunicorn web_personal.wsgi
python manage.py migrate
chmod a+x build.sh

