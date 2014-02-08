from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from core.views import HomepageView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r"^$", HomepageView.as_view()),
    url(r'^api/', include("activities.urls")),

    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
