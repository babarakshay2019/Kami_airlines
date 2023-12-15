import math

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from .models import Airplane
from .serializers import AirplaneSerializer


class AirplaneTests(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Create sample data for testing
        self.airplane_data = {"id": 1, "passenger_assumptions": 100}
        self.airplane = Airplane.objects.create(**self.airplane_data)

    def test_airplane_model(self):
        self.assertEqual(self.airplane.passenger_assumptions, 100)
        self.assertEqual(self.airplane.fuel_tank_capacity_liters(), 200)
        self.assertAlmostEqual(
            self.airplane.fuel_consumption_per_minute(),
            0.80 * math.log(1) + 0.002 * 100,
            places=2,
        )

    def test_airplane_serializer(self):
        serializer = AirplaneSerializer(instance=self.airplane)

        self.assertEqual(serializer.data["id"], 1)
        self.assertEqual(serializer.data["passenger_assumptions"], 100)
        self.assertIn("fuel_consumption_per_minute", serializer.data)
        self.assertIn("max_airplane_fly_time", serializer.data)
        self.assertIsInstance(serializer.data["fuel_consumption_per_minute"],
                              float)
        self.assertIsInstance(serializer.data["max_airplane_fly_time"], float)

    def test_list_airplanes(self):
        url = reverse("airplane-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            len(response.data), 1
        )  # Assuming there is one airplane in the database

    def test_create_airplane(self):
        url = reverse("airplane-list")
        new_airplane_data = {"id": 2, "passenger_assumptions": 200}
        response = self.client.post(url, data=new_airplane_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Verify the new airplane is in the database
        self.assertEqual(Airplane.objects.count(), 2)

        # Verify the response data matches the created object
        self.assertEqual(response.data["id"], new_airplane_data["id"])
        self.assertEqual(
            response.data["passenger_assumptions"],
            new_airplane_data["passenger_assumptions"],
        )

    def test_invalid_create_airplane(self):
        url = reverse("airplane-list")
        # Test creating an airplane with invalid data
        invalid_airplane_data = {"id": 3, 
                                 "passenger_assumptions": "invalid_data"}
        response = self.client.post(url, data=invalid_airplane_data,
                                    format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
