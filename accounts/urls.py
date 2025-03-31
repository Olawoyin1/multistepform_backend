from django.urls import path
from .views import SendOTPView, VerifyOTPView, RegisterUserView, AllUsersActions, ResendOTPView


urlpatterns = [
    path('send-otp/', SendOTPView.as_view(), name='send-otp'),
    path('verify-otp/', VerifyOTPView.as_view(), name='verify-otp'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('resend-otp/', ResendOTPView.as_view(), name='resend_otp'),
    path('users/<str:pk>/', AllUsersActions.as_view(), name='users'),
]
