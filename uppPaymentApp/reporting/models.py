from django.db import models

class Reporting(models.Model):  
    townName = models.CharField(max_length=200)
    timeOfDay = models.CharField(max_length=200)
    def __str__(self):
         return 'Name of object: ' + self.name 