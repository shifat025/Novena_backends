from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import Contact


router = DefaultRouter()
router.register('',Contact)

urlpatterns = [
    path('',include(router.urls)),
]