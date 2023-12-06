# from django.db import models
from datetime import date, datetime
from email.policy import default
from typing_extensions import Required
from django.db import models
from authentication.models import User
from authentication.serializers import userSerializer

from project.models import Project 
class Remotework(models.Model):
        
    STATUS_OPTIONS=[
        ('APPROVED','APPROVED'),
        ('INPROGRESS','INPROGRESS'),
        ('DECLINED','DECLINED'),
    ]
    name=models.TextField(max_length=255)
    position=models.TextField(max_length=255)
    nbdays=models.PositiveIntegerField(null=False,blank=False)
    createdate= models.DateField(null=False,blank=False)
    startdate=models.DateField(null=False,blank=False)
    returndate= models.DateField(null=False,blank=False)
    motif=models.TextField(max_length=255)
    creator=models.ForeignKey(to=User,on_delete=models.CASCADE,default=3)
    status=models.CharField(choices=STATUS_OPTIONS,max_length=255)

class Remoteworkplan(models.Model):
    STATUS_OPTIONS=[
        ('TO DO','TO DO'),
        ('INPROGRESS','INPROGRESS'),
    ]
    date= models.DateField(null=False,blank=False)
    task=models.TextField(max_length=255)
    status=models.CharField(choices=STATUS_OPTIONS,max_length=255)
    request=models.ForeignKey(to=Remotework,on_delete=models.CASCADE,default=3)
    # remotework = models.ForeignKey(Remotework, on_delete=models.CASCADE, related_name='remotework_plans')

