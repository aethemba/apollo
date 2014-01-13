
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, generics
from api.serializers import UserSerializer, ActivitySerializer
from api.models import Activity

class UserViewSet(viewsets.ModelViewSet):
	"""
	API Endpoint for users
	"""
	queryset = User.objects.all()
	serializer_class = UserSerializer


class ActivityList(generics.ListAPIView):
	"""
	API Endpoint for Activities
	"""
	queryset = Activity.objects.all()
	serializer_class = ActivitySerializer


class UserList(generics.ListAPIView):
	"""
	API Endpoint for Users
	"""
	queryset = User.objects.all()
	serializer_class = UserSerializer


class ActivityDetail(generics.RetrieveUpdateDestroyAPIView):
	"""
	API Endpoint for a single Activity
	"""
	queryset = Activity.objects.all()
	serializer_class = ActivitySerializer

	def pre_save(self, obj):
		print self
		print obj
		obj.user = self.request.user
