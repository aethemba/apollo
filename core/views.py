from django.contrib.auth.models import User
from django.views.generic.base import TemplateView
from rest_framework import viewsets, generics
from .serializers import UserSerializer


class HomepageView(TemplateView):
    template_name="core/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomepageView, self).get_context_data(**kwargs)
        context['loops'] = [n for n in range(15)]
        return context


class UserList(generics.ListCreateAPIView):
    """
	API Endpoint for Users
	"""
    queryset = User.objects.all()
    serializer_class = UserSerializer