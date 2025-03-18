from rest_framework import serializers
from .models import Trainee, Track

class TraineeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainee
        fields = '__all__'

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = '__all__'