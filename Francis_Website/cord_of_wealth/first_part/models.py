from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from datetime import datetime
import uuid, random
from django.utils import timezone
from django.urls import reverse
from datetime import timedelta
from django.utils.timezone import now
from django.core.validators import RegexValidator
from .forms import UserRegistrationForm



# from django.core.validators import MinLenghtValidator
# Create your models here.
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    body = models.CharField(max_length=500)

class Signup(UserRegistrationForm):
    phone = models.CharField(max_length=15, validators=[RegexValidator(regex=r'^\+?1?\d{10,}$', message="Phone number must be in the format: '+234-xxx-xxxx-xxx' with up to 10 digits.")])
    class Meta:
        model = User
        fields = ["username", "email", "phone", "password1", "password2"]

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    phone = models.CharField(max_length=15, validators=[RegexValidator(regex=r'^\+?1?\d{10,}$', message="Phone number must be in the format: '+234-xxx-xxxx-xxx' with up to 10 digits.")])
    





