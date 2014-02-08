from django.contrib.auth.models import User
from rest_framework import viewsets, generics
from core.serializers import UserSerializer
from .serializers import ActivitySerializer
from .models import Activity

class ActivityList(generics.ListCreateAPIView):
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
    def pre_save(self, obj):
        print self
        print obj
        print self.request.user
        obj.user = self.request.user



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
