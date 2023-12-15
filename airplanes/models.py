"""Models module defining the Airplane model."""
import math

from django.db import models


class Airplane(models.Model):
    """Model representing an airplane with specific attributes and methods."""

    id = models.PositiveIntegerField(primary_key=True)
    passenger_assumptions = models.PositiveIntegerField()

    def fuel_tank_capacity_liters(self):
        """
        Calculate and return the fuel tank capacity in liters based on the
           airplane's ID."""
        return 200 * self.id

    def fuel_consumption_per_minute(self):
        """Calculate and return the fuel consumption per minute for the 
           airplane."""
        base_fuel_consumption = 0.80 * math.log(self.id)
        passenger_fuel_consumption = 0.002 * self.passenger_assumptions
        return base_fuel_consumption + passenger_fuel_consumption

    def max_airplane_fly_time(self):
        """Calculate and return the maximum fly time for the airplane."""
        fuel_consumed_per_minute = self.fuel_consumption_per_minute()
        return self.fuel_tank_capacity_liters() / fuel_consumed_per_minute

    def __str__(self):
        """Return a string representation of the airplane object."""
        return f"Airplane {self.id}"
