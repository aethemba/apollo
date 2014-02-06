from django.conf.urls import patterns, include, url
from django.views.generic.base import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from apollo_ember.views import HomepageView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r"^$", HomepageView.as_view()),
    url(r'^api/', include("api.urls")),
    # url(r'^apollo/', include('apollo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
