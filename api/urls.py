from django.conf.urls import patterns, include, url
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, routers
from api import views

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"groups", views.GroupViewSet)

urlpatterns = patterns("",
    url(r'^', include(router.urls) ),
    url(r'^api-auth/', include('rest_framework.urls', namespace="rest_framework") )
)
