# from django.db import models
from datetime import date, datetime
from email.policy import default
from typing_extensions import Required
from django.db import models
from authentication.models import User
from authentication.serializers import userSerializer

from project.models import Project 
class Meetingroom(models.Model):
        
    STATUS_OPTIONS=[
        ('APPROVED','APPROVED'),
        ('DECLINED','DECLINED'),
        ('INPORGRESS','INPROGRESS'),
    ]
    ROOM_OPTIONS=[
        ('ROOM1','ROOM1'),
        ('ROOM2','ROOM2'),
    ]
    name=models.TextField(default="")
    room=models.CharField(choices=ROOM_OPTIONS,max_length=255)
    purpose=models.TextField(max_length=255)
    creator=models.ForeignKey(to=User,on_delete=models.CASCADE,default=3)
    createdate= models.DateField(null=False,blank=False)
    startdate=models.DateField(null=False,blank=False)
    enddate= models.DateField(null=False,blank=False)
    status=models.CharField(choices=STATUS_OPTIONS,max_length=255)




