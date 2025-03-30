from rest_framework import serializers
from .models import OTPVerification


class SendOTPSerializer(serializers.ModelSerializer):
    class Meta:
        model= OTPVerification
        fields = ['email', 'first_name', 'last_name', 'phonenumber', 'dob', 'gender']