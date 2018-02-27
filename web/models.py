from django.db import models

class Userinfo(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=50,null=True)  #可以为空
    password=models.CharField(max_length=50,null=False)  #不能为空
    Gender = models.BooleanField(default=False)
    Age = models.IntegerField(default=28)
    memo = models.TextField(default='lalallalala')
    CreatData = models.DateTimeField(default='2018-1-12')
    user_type= models.ForeignKey('UserTpye')

class UserTpye(models.Model):
    name=models.CharField(max_length=50)


class ass(models.Model):
    hostname=models.CharField(max_length=20)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True,error_messages={'invalid':'日期格式错误'})

class Userinfo_temp(models.Model):

    ROLE_CHOICE = (
        (u'1',u'普通用户'),
        (u'2',u'管理员'),
        (u'3',u'超级管理员')
    )
    UserType = models.CharField(max_length=2,choices=ROLE_CHOICE)

#自定义分页数据库
class hostip(models.Model):
    host=models.CharField(max_length=20)
    ip=models.CharField(max_length=20)
