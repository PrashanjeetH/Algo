from django.db import models
from django.contrib.auth.models import User


class UserDataModel(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE,)
    data = models.CharField(max_length=2000)
    # record_file = models.FileField(upload_to='media%H%M%S')
    created_on = models.DateTimeField(auto_now_add=True,)

    class Meta:
        verbose_name_plural = 'Records'
        db_table = "User Records"

    def __str__(self):
        return f"{self.username} | {self.created_on.strftime('%d/%m/%y')}"
