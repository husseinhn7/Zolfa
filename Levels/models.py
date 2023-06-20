from django.db import models


# Create your models here.


class Level(models.Model):
    level_name         = models.CharField( max_length=100)
    number_of_students = models.IntegerField()
    start_date         = models.DateField( auto_now=False, auto_now_add=False)
    end_date           = models.DateField( auto_now=False, auto_now_add=False)
    level_statues      = models.BooleanField()
    
    



