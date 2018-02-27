from django.db import models

class  UserInfo(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    email=models.EmailField()

class UserGroup(models.Model):
    GroupName=models.CharField(max_length=50)
    user=models.ManyToManyField('UserInfo')