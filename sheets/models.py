from django.db import models
from datetime import date, datetime, time

# Create your models here.

class Orders(models.Model):
    firstname = models.CharField(max_length=100,null=False,blank=True)
    lastname = models.CharField(max_length=100)
    created_on = models.DateField(auto_now=True)
    price = models.IntegerField(null=False)
    status = models.CharField(max_length=100)
    
    
    class Meta:
        db_table = "orders"
        
    def __str__(self):
        return self.firstname + " " + self.lastname
    
    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)
        
class ExcelFileUpload(models.Model):
    excel_file_upload = models.FileField(upload_to="excel")
