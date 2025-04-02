from rest_framework import serializers
from .models import OTPVerification, User


class SendOTPSerializer(serializers.ModelSerializer):
    class Meta:
        model= OTPVerification
        fields = ['email', 'first_name', 'last_name', 'phonenumber', 'dob', 'gender']



class VerifyOTPSerializer(serializers.ModelSerializer):
    class Meta:
        model= OTPVerification
        fields = ['email', 'otp_code', 'first_name', 'last_name', 'phonenumber', 'dob', 'gender']



class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = '__all__'


# ✅ Step 3: Final User Registration
class PasswordSetupSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate_email(self, value):
        # Ensure email exists and is verified before proceeding
        if not User.objects.filter(email=value, is_email_verified=True).exists():
            raise serializers.ValidationError("Email not registered or not verified.")
        return value

    def update_password(self):
        """Update the password for the existing user"""
        email = self.validated_data["email"]
        password = self.validated_data["password"]
        
        # Get user and set new password
        user = User.objects.get(email=email)
        user.set_password(password)
        user.save()
        return user