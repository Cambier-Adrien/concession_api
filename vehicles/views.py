from django.shortcuts import render
from rest_framework import viewsets
from .models import Concession, Vehicule
from .serializers import ConcessionSerializer, VehicleSerializer

# Create your views here.
class ConcessionViewSet(viewsets.ModelViewSet):
    queryset = Concession.objects.all()
    serializer_class = ConcessionSerializer


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicule.objects.all()
    serializer_class = VehicleSerializer