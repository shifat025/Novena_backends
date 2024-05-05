from django.db import models
from patient.models import Patient
from doctor.models import Doctor,AvailableTime

# Create your models here.
Appointment_Status = [
    ('Completed','Completed'),
    ('Pending','Pending'),
    ('Running','Running'),
]
Appointment_Type = [
    ('Offline','Offline'),
    ('Online','Online'),
]
class Appointment(models.Model):
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    docter = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    appointment_types = models.CharField(choices=Appointment_Type,max_length=10)
    appointment_status = models.CharField(choices=Appointment_Status,max_length=15,default='Pending')
    symtom = models.TextField()
    time = models.ForeignKey(AvailableTime,on_delete=models.CASCADE)
    cancel = models.BooleanField(default=False)

    def __str__(self):
        return f"Doctor : {self.docter.user.first_name}, Patient : {self.patient.user.first_name}"
