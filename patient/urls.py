from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import Patientviewset


router = DefaultRouter()
router.register('list',Patientviewset)

urlpatterns = [
    path('',include(router.urls)),

]