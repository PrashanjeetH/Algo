from django.db import models
from django.contrib.auth.models import User


class UserDataModel(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE, )
    data = models.CharField(max_length=2000)
    created_on = models.DateTimeField(auto_now_add=True)
