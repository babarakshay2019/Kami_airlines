"""Views module defining AirplaneViewSet for handling airplane-related API
   requests."""
from rest_framework import viewsets

from .models import Airplane
from .serializers import AirplaneSerializer


class AirplaneViewSet(viewsets.ModelViewSet):
    """ViewSet for handling CRUD operations on Airplane objects."""
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer
