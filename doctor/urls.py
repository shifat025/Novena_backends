from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import Doctorviewset,AvailableTimeviewset,Reviewviewset


router = DefaultRouter()
router.register('list',Doctorviewset)
router.register('availabletime',AvailableTimeviewset)
router.register('review',Reviewviewset)

urlpatterns = [
    path('',include(router.urls)),

]