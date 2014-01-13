from django.contrib.auth.models import User
from rest_framework import serializers
from api.models import Activity

class UserSerializer(serializers.ModelSerializer):
	activities = serializers.PrimaryKeyRelatedField(many=True)

	class Meta:
		model = User
		fields = ("id", "username", "email", "activities")

class ActivitySerializer(serializers.ModelSerializer):
	class Meta:
		model = Activity
		fields = ("name", "category", "description")