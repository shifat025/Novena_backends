from django.shortcuts import render
from .serializers import ContactSerializer
from .models import ContactUs
from rest_framework import viewsets

# Create your views here.

class Contact(viewsets.ModelViewSet):
    queryset = ContactUs.objects.all()
    serializer_class = ContactSerializer