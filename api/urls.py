from django.conf.urls import patterns, include, url
from django.contrib.auth.models import User, Group
from api import views


urlpatterns = patterns("",
    url(r'^users/$', views.UserList.as_view()),
   # url(r'^users/(?P<pk>[0-9]+)$', views.UserDetail),
    url(r'^activities/$', views.ActivityList.as_view() ),
    url(r'^activities/(?P<pk>[0-9]+)$', views.ActivityDetail.as_view() ), 
    url(r'^api-auth/', include('rest_framework.urls', namespace="rest_framework") )
)
