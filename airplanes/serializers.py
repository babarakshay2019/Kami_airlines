"""Serializers module defining AirplaneSerializer for converting Airplane 
   objects to/from JSON."""
from rest_framework import serializers

from .models import Airplane


class AirplaneSerializer(serializers.ModelSerializer):
    """Serializer for the Airplane model, including custom methods for
       additional fields."""

    fuel_consumption_per_minute = serializers.SerializerMethodField()
    max_airplane_fly_time = serializers.SerializerMethodField()

    class Meta:
        model = Airplane
        fields = [
            "id",
            "passenger_assumptions",
            "fuel_consumption_per_minute",
            "max_airplane_fly_time",
        ]

    def get_fuel_consumption_per_minute(self, obj):
        """Return the fuel consumption per minute for the given Airplane 
           object."""
        return round(obj.fuel_consumption_per_minute(), 2)

    def get_max_airplane_fly_time(self, obj):
        """Return the maximum fly time for the given Airplane object."""
        return round(obj.max_airplane_fly_time(), 2)
