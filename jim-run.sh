#!/bin/bash 
docker run --name jim-django-app -v "$PWD/mysite":/usr/src/app -w /usr/src/app -p 8000:8000 -ti django bash -c "pip install --proxy=http://10.241.104.240:5678/ -r requirements.txt && /bin/bash"
