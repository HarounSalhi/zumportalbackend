from django.db import models




class Room(models.Model):
    name = models.CharField(max_length=100)
    dispo = models.IntegerField()
    capacity = models.IntegerField(null=True,blank=True)
    

  

class Equipement(models.Model):
    name_eq = models.CharField(max_length=100)
    dispo_eq= models.IntegerField()
    start_hour_eq = models.CharField(max_length=100)
    finish_hour_eq = models.CharField(max_length=100)
    type = models.CharField(max_length=100) 
    
class RequestRooms(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField(null=True, blank=True)
    start_hour = models.TimeField()  # Use TimeField to store time
    finish_hour = models.TimeField()  # Use TimeField to store time
    description = models.CharField(max_length=200)
    etat = models.IntegerField(null=True)
   





# Create your models here.
