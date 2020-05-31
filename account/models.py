from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    real_name = models.CharField(max_length=100)
    time_zone = models.CharField(max_length=50)
    create_time = models.DateTimeField(auto_now_add=True)
    user_name = models.CharField(max_length=50, unique=True)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()
    USERNAME_FIELD = 'user_name'

    def __str__(self):
        return self.user_name


class ActivityPeriods(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='activity_periods')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()


