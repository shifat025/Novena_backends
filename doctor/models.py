from django.db import models
from django.contrib.auth.models import User
from patient.models import Patient

# Create your models here.

class Speacialization(models.Model):
    name = models.CharField(max_length=40)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.name

class Designation(models.Model):
    name = models.CharField(max_length=40)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.name

class AvailableTime(models.Model):
    name = models.CharField(max_length=50)


    def __str__(self):
        return self.name
    

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    image = models.ImageField(upload_to='doctor/media/uploads', blank=True, null=True)
    designation = models.ManyToManyField(Designation)
    specialization = models.ManyToManyField(Speacialization)
    availabletime = models.ManyToManyField(AvailableTime)
    fee = models.IntegerField()
    meet_link = models.CharField(max_length=100)

    def __str__(self):
        return f"Dr. {self.user.first_name} {self.user.last_name}"
    
star_choice = [
    ('⭐','⭐'),
    ('⭐⭐','⭐⭐'),
    ('⭐⭐⭐','⭐⭐⭐'),
    ('⭐⭐⭐⭐','⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐','⭐⭐⭐⭐⭐'),
]
class Review(models.Model):
    reviewer = models.ForeignKey(Patient, on_delete=models.CASCADE)
    docter = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    ratting = models.CharField(choices=star_choice,max_length=10)

    def __str__(self):
        return f"Patient: {self.reviewer.user.first_name}; Doctor: {self.docter.user.first_name}"