#
# 
#
FROM django:onbuild
MAINTAINER jim_lin <jim_lin@quantatw.com> 
ADD app/. /usr/src/app/
EXPOSE 8000
CMD ["python", "manage.py runserver"]
