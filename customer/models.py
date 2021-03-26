from django.db import models
from django.contrib.auth.models import AbstractUser

class Userauth(AbstractUser):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=50, unique=True, error_messages={'unique': "Username already exists"})
    password = models.CharField(max_length=8)
    email = models.CharField(max_length=50)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'

    def __str__(self):
        return str(self.id) +' '+ self.username
