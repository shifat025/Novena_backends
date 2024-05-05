from django.shortcuts import render
from .serializers import ServiceSerializer
from .models import Service
from rest_framework import viewsets

# Create your views here.

class Services(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer