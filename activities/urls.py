from django.conf.urls import patterns, include, url
from django.contrib.auth.models import User, Group
from core.views import UserList
from .views import ActivityDetail, ActivityList


urlpatterns = patterns("",
    url(r'^users/$', UserList.as_view()),
    #url(r'^users/(?P<pk>[0-9]+)$', views.UserDetail),
    url(r'^activities/$', ActivityList.as_view() ),
    url(r'^activities/(?P<pk>[0-9]+)$', ActivityDetail.as_view() ),
)
