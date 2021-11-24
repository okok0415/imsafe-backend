from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import date
from PIL import Image


class User(AbstractUser):
    password = models.CharField(max_length=255)
