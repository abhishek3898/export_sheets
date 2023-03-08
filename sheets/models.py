from django.db import models
from datetime import date, datetime, time

# Create your models here.

class Orders(models.Model):
    firstname = models.CharField(max_length=100,null=False,blank=True)
    lastname = models.CharField(max_length=100)
    created_on = models.DateField(auto_now=True)
    price = models.IntegerField(null=False)
    status = models.CharField(max_length=100)
    
    def __str__(self):
        self.firstname + " " + self.lastname
    
    class Meta:
        db_table = "orders"