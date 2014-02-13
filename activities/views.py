from django.contrib.auth.models import User
from rest_framework import viewsets, generics
from core.serializers import UserSerializer
from .serializers import ActivitySerializer
from .models import Activity
from rest_framework.renderers import JSONRenderer

class EmberJSONRenderer(JSONRenderer):

    def render(self, data, accepted_media_type=None, renderer_context=None):
        print data
        data = {'activity' : data }
        return super(EmberJSONRenderer, self).render(data, accepted_media_type, renderer_context)


class ActivityList(generics.ListCreateAPIView):
    """
	API Endpoint for Activities
	"""
    renderer_classes = (EmberJSONRenderer,)

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
    renderer_classes = (EmberJSONRenderer,)

    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

    def pre_save(self, obj):
        print self
        print obj
        obj.user = self.request.user
