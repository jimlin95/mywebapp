from django.contrib import admin

# Register your models here.
from django.contrib import admin

from lcsw.models import Excuse, Article, Category

admin.site.register(Excuse)
admin.site.register(Article)
admin.site.register(Category)
