from rest_framework import serializers
from .models import Plant, Watering


class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = ['id', 'title', 'description']


class WateringSerializer(serializers.ModelSerializer):
    class Meta:
        model = Watering
        fields = ['id', 'date']
