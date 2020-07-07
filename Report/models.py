from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
 
# Create your models here.
class Finance_Report(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    salary=models.IntegerField(("salary"),null=True)
    investment=models.IntegerField(("investment"),null=True)
    total=models.IntegerField("total",null=True)
    timestamp=models.DateTimeField(auto_now=True)
    payment=models.BooleanField("process vendor payment",default=True)
    created=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        print("username",self.user.username)
        return self.user.username

    
    
    def get_absolute_url(self):
        return reverse("report:finance-report")
    

 