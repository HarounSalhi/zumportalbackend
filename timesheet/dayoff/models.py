# from django.db import models
from datetime import date, datetime
from email.policy import default
from typing_extensions import Required
from django.db import models
from authentication.models import User
from authentication.serializers import userSerializer

from project.models import Project 
class Dayoff(models.Model):
        
    STATUS_OPTIONS=[
        ('APPROVED','APPROVED'),
        ('INPROGRESS','INPROGRESS'),
        ('DECLINED','DECLINED'),
    ]
    TYPE_OPTIONS=[
        ('EMERGENCY LEAVE','EMMERGENCY LEAVE'),
        ('ANNUAL LEAVE','ANNUAL LEAVE'),
        ('PERSONAL LEAVE','PERSONAL LEAVE'),
        ('RECOVERY LEAVE','RECOVERY LEAVE'),
    ]
    name=models.TextField(max_length=255,default='default')
    position=models.TextField(max_length=255,default='default')
    nbdays=models.PositiveIntegerField(null=False,blank=False,default=0)
    type=models.CharField(choices=TYPE_OPTIONS,max_length=255)
    createdate= models.DateField(null=False,blank=False,default=datetime.now().date())
    startdate=models.DateField(null=False,blank=False,default=datetime.now().date())
    returndate= models.DateField(null=False,blank=False,default=datetime.now().date())
    backupperson=models.ForeignKey(to=User,related_name="backupperson",on_delete=models.CASCADE,default=3)
    motif=models.TextField(max_length=255,default='default')
    creator=models.ForeignKey(to=User,related_name="dayoffcreator",on_delete=models.CASCADE,default=3)
    status=models.CharField(choices=STATUS_OPTIONS,max_length=255,default="INPROGRESS")
