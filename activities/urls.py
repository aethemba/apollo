from django.conf.urls import patterns, include, url
from django.contrib.auth.models import User, Group
from .views import ActivityDetail, ActivityList, UserList


urlpatterns = patterns("",
    url(r'^users/$', UserList.as_view()),
    #url(r'^users/(?P<pk>[0-9]+)$', views.UserDetail),
    url(r'^activities/$', ActivityList.as_view() ),
    url(r'^activities/(?P<pk>[0-9]+)$', ActivityDetail.as_view() ),
    url(r'^api-auth/', include('rest_framework.urls', namespace="rest_framework") )
)
