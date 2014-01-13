from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Activity(models.Model):
	name = models.CharField(max_length=255)
	created = models.DateTimeField()
	updated = models.DateTimeField()
	category = models.ForeignKey("Category", blank=True, null=True)

	description = models.TextField(blank=True)
	user = models.ForeignKey(User, related_name="activities")


	def save(self, *args, **kwargs):
		if not self.id:
			self.created = datetime.now()
		self.updated = datetime.now()
		super(Activity, self).save(*args, **kwargs)

class Category(models.Model):
	name = models.CharField(max_length=255)