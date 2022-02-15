from django.db import models

class Payment(models.Model):  
    name = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    decription = models.CharField(max_length=200)
    def __str__(self):
         return 'Name of object: ' + self.name 