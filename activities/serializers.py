from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Activity
from django.conf import settings
from micawber.contrib.mcdjango import providers
from micawber.exceptions import ProviderException
from micawber.parsers import standalone_url_re, full_handler

class UserSerializer(serializers.ModelSerializer):
    activities = serializers.PrimaryKeyRelatedField(many=True)

    class Meta:
        model = User
        fields = ("id", "username", "email", "activities")

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        resource_name = 'activity'
        fields = ("id", "name", "category", "description")

class OEmbedField(serializers.Field):
    def __init__(self, source, maxwidth=None, maxheight=None, **kwargs):
        super(OEmbedField, self).__init__(source)
        self.params = getattr(settings, 'MICAWBER_DEFAULT_SETTINGS', {})
        self.params.update(kwargs)
        # enforce HTTPS, see https://groups.google.com/forum/?fromgroups#!topic/youtube-activities-gdata/S9Fa-Zw2Ma8
        self.params['scheme'] = 'https'
        if maxwidth and maxheight:
            self.params['maxwidth'] = maxwidth
            self.params['maxheight'] = maxheight
        elif maxwidth:
            self.params['maxwidth'] = maxwidth
            self.params.pop('maxheight', None)

    def to_native(self, value):
        if not value or not standalone_url_re.match(value):
            return ""
        url = value.strip()
        if value == 'https://vimeo.com/85425318':
            return "<iframe src=\"//player.vimeo.com/video/85425318\" hard=\"code\" width=\"1024\" height=\"576\" frameborder=\"0\" title=\"How it works - Cares\" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>"
        try:
            response = providers.request(url, **self.params)
        except ProviderException:
            return ""
        except URLError:
            return ""
        else:
            html = full_handler(url, response, **self.params)
            # Tweak for youtube to hide controls and info bars.
            html = html.replace('feature=oembed', 'feature=oembed&showinfo=0&controls=0')
            return html

