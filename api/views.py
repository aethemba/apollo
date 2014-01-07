
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from api.serializers import UserSerializer, GroupSerializer

class UserViewSet(viewsets.ModelViewSet):
	"""
	API Endpoint for users
	"""

	queryset = User.objects.all()
	serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
	"""
	API Endpoint for GroupSerializer
	"""
	queryset = Group.objects.all()
	serializer_class = GroupSerializer


