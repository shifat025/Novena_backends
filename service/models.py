from django.db import models

# Create your models here.

class Service(models.Model):
    name = models.CharField(max_length=50)
    discription = models.TextField()
    image = models.ImageField(upload_to='service/media/uploads', blank=True, null=True)

    def __str__(self):
        return self.name