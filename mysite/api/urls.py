from django.conf.urls import patterns, url
import api
urlpatterns = [
    url(r'^tasks/$', api.task_list.as_view()),
    url(r'^tasks/(?P<pk>[0-9]+)$', api.views.task_detail.as_view())
]
