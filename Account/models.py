from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user=models.OneToOneField(User, verbose_name=("user"), on_delete=models.CASCADE)
    email=models.EmailField(max_length=30)
    
    

    class Meta:
        permissions = (
            ('Finance_Manager','approve payments to vendor'),
            ('Analyst','process vendor payment')
        )

    def __str__(self):
        return self.user.username
    