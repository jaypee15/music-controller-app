from rest_framework import serializers
from .models import Room

class RoomSerializers(serializers.ModelSerializer):
    class Meta:
        models = Room
        fields = ('id', 'code', 'host', 'guest_can_pause', 'votes_to_skip', 'created_at')