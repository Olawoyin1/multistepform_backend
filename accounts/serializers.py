from rest_framework import serializers
from .models import OTPVerification, User


class SendOTPSerializer(serializers.ModelSerializer):
    class Meta:
        model= OTPVerification
        fields = ['email', 'first_name', 'last_name', 'phonenumber', 'dob', 'gender']



class VerifyOTPSerializer(serializers.ModelSerializer):
    class Meta:
        model= OTPVerification
        fields = ['email', 'otp_code',]



class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = '__all__'


class PasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model: User
        fields = ['email', 'password']