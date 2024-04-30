from django.urls import path, include
from .views import  RegisterAPIView ,EmailVerificationView,UserLogin,UserLogout,UserDetailView
from rest_framework.routers import DefaultRouter


# router = DefaultRouter()
# router.register()

urlpatterns = [
    path('registration/', RegisterAPIView.as_view(), name='registration'),
    path('activate/<uid64>/<token>/', EmailVerificationView.as_view(), name='email-verification'),
    path('login/', UserLogin.as_view(), name='Login'),
    path('logout/', UserLogout.as_view(), name='Logout'),
    path('user_details/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    
]