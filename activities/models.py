from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from sorl.thumbnail import ImageField
from djchoices.choices import DjangoChoices, ChoiceItem

class Activity(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(_('slug'), max_length=100, unique=True)

    created = models.DateTimeField()
    updated = models.DateTimeField()

    category = models.ManyToManyField("Category", blank=True, null=True)

    image = ImageField(
        _('image'), max_length=255, blank=True, upload_to='images/',
        help_text=_('image document'))

    description = models.TextField(blank=True)
    user = models.ForeignKey(User, related_name="activity")

    embed_url = models.URLField(
        _('video'), max_length=100, blank=True, null=True, default='',
        help_text=_(""))

    file = models.FileField(upload_to='documents/%Y/%m/%d')

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = datetime.now()
        self.updated = datetime.now()
        super(Activity, self).save(*args, **kwargs)


class Category(models.Model):
    name = models.CharField(max_length=255)
