from rest_framework import serializers
from .models import Capsule

class CapsuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Capsule
        fields = ['content', 'picture', 'destination', 'open_date']