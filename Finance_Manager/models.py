from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class FinanceManager(models.Model):
    user=models.ForeignKey(User, verbose_name=("user"), on_delete=models.CASCADE)
    approve_payments=models.BooleanField("approve payments to vendor",default=True)

    def __str__(self):
        return self.user.username
    