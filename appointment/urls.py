from django.urls import path, include
from rest_framework import routers
from .views import Appointmentviewset

router = routers.DefaultRouter()
router.register('appointment',Appointmentviewset)

urlpatterns = [
    path('',include(router.urls)),
]