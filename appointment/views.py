from django.shortcuts import render
from rest_framework import viewsets
from .models import Appointment
from .serializers import AppoinmentSerializers
# Create your views here.

class Appointmentviewset(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppoinmentSerializers

    # custom query
    def get_queryset(self):
        queryset =  super().get_queryset()
        patient_id = self.request.query_params.get('patient_id')
        if patient_id:
            queryset = queryset.filter(patient_id = patient_id)
        return queryset

