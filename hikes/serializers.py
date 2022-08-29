from rest_framework import serializers
from .models import Hike

class HikeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'owner', 'name', 'description', 'created_at')
        model = Hike
