from django.db import models

# Create your models here.
class Items(models.Model):
    url = models.CharField(max_length=500)
    date = models.DateField()
    user = models.CharField(max_length=40)
    
