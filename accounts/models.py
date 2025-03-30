from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser

# Create your models here.
class BaseUserManger(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Please provide an Email Address")
        email = self.normalize_email(email)
        
        user = self.model(email=email, **extra_fields)
        if password:
            user.set_password(password)
        user.save()
        return user




    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)
    
    
    
    
class User(AbstractUser):
    GENDER_CHOICES = (
        ('male', 'male'),
        ('female', 'female')
    )

    email = models.EmailField(unique=True)
    is_email_verified = models.BooleanField(default=False)
    phonenumber = models.CharField(max_length=14)
    dob = models.DateField(null=True, blank=True) 
    gender = models.CharField(
        max_length=10, choices=GENDER_CHOICES, null=True, blank=True
    )
    username=None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = BaseUserManager()

    def __str__(self):
        return self.email
    