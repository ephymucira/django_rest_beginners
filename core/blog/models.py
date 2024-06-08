from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Cars(models.Model):
    car_name = models.CharField(max_length=100)
    car_version = models.CharField(max_length=3)
    car_model = models.CharField(max_length=30)