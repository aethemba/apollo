from django.contrib.auth.models import User, Group
from rest_framework import viewsets, generics
from .serializers import UserSerializer, ActivitySerializer
from .models import Activity


class ActivityList(generics.ListAPIView):
    """
	API Endpoint for Activities
	"""
    model = Activity
    #queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    paginate_by = None
    # def get_queryset(self):
    #
    #     return Activity.objects.all()


class UserList(generics.ListCreateAPIView):
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
