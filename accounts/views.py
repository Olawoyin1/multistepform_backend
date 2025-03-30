from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import SendOTPSerializer
from .models import OTPVerification
from django.utils import timezone
from decouple import config
import requests

# Create your views here.

BREVO_API_KEY = config("BREVO_API_KEY")
SENDER_EMAIL = config("SENDER_EMAIL")


def send_otp_email(to_email, subject, body):
    """
    Sends an email using the Brevo (Sendinblue) API.
    """
    url = "https://api.brevo.com/v3/smtp/email"
    headers = {
        "api-key": BREVO_API_KEY,
        "Content-Type": "application/json"
    }
    data = {
         "sender": {
            "name": "Study Lab 📚",  #  Set your desired display name here
            "email": SENDER_EMAIL  # Must be a verified email in Brevo
        },
        "to": [{"email": to_email}],
        "subject": subject,
        "textContent": body
    }

    try:
        response = requests.post(url, headers=headers, json=data, timeout=10)  # Added timeout
        response.raise_for_status()  # Raises an error for HTTP 4xx or 5xx
        return response
    except requests.exceptions.Timeout:
        print("❌ ERROR: Connection to Brevo API timed out.")
        return None
    except requests.exceptions.RequestException as e:
        print(f"❌ ERROR: {e}")
        return None









class SendOTP(APIView):
    def post(self,request, *args, **kwargs):
        user_data = request.data
        serializer = SendOTPSerializer(data=user_data)
        
        try:
            user = serializer.validated_data
            generated_otp_code = OTPVerification.generate_OTP()
            
            OTPVerification.objects.create(
                email=user['email'],
                otp_code=generated_otp_code,
                first_name=user['first_name'],
                last_name=user['last_name'],
                phonenumber=user['phonenumber'],
                dob=user['dob'],
                gender=user['gender'],
                created_at=timezone.now()
            )
            
            
            # Send OTP email
            subject = "Your OTP Verification Code"
            body = f"""
            Dear {user['first_name']},
            
            Welcome to Study Lab! To complete your registration, please verify your email using the One-Time Password (OTP) below:

            Your OTP verification code is: {generated_otp_code}
            
            This code is valid for 10 minutes. If you didn’t request this, please ignore this email.

            Need help? Contact our support team anytime.

            Happy Learning! 📚
            The Study Lab Team
            """

            response = send_otp_email(user['email'], subject, body)
            
            
            
        except Exception as e:
            pass