from django.shortcuts import render
from .serializers import DoctorSerializer,SpeacializationSerializer,DesignationSerializer,AvailableTimeSerializer,ReviewSerializer
from .models import Doctor,Speacialization,Designation,AvailableTime,Review
from rest_framework import viewsets

# Create your views here.

class Doctorviewset(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

# class Speacializationviewset(viewsets.ModelViewSet):
#     queryset = Speacialization.objects.all()
#     serializer_class = SpeacializationSerializer

# class Designationviewset(viewsets.ModelViewSet):
#     queryset = Designation.objects.all()
#     serializer_class = DesignationSerializer


class AvailableTimeviewset(viewsets.ModelViewSet):
    queryset = AvailableTime.objects.all()
    serializer_class = AvailableTimeSerializer

class Reviewviewset(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer