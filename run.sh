#!/bin/bash 
docker run --name some-django-app -v "$PWD/mysite":/usr/src/app -w /usr/src/app -p 8000:8000 -d django bash -c "pip install --proxy=http://10.241.104.240:5678/ -r requirements.txt && python manage.py runserver 0.0.0.0:8000"
