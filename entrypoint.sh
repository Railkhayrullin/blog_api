#! /bin/bash

python manage.py makemigrations

python manage.py migrate

python manage.py initadmin

python manage.py initusers

python manage.py initmockdata

python manage.py runserver 0.0.0.0:8000