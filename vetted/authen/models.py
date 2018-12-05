from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    company = models.CharField(blank=False,max_length=20)
    def __str__(self):
      return self.user.username

class CompanyInfo(models.Model):
    name = models.CharField(blank=False,max_length=20)
    description = models.CharField(blank=False,max_length=20)
    def __str__(self):
      return self.name

class AdminProfileInfo(models.Model):
    employee = models.ForeignKey(User,on_delete=models.CASCADE)
    company = models.ForeignKey(CompanyInfo,on_delete=models.CASCADE)
    def __str__(self):
      return self.employee.username
