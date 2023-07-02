from django.db import models
from Users.models import User

# Create your models here.


class Level(models.Model):
    name               = models.CharField( max_length=100)
    start_date         = models.DateField( auto_now=False, auto_now_add=False)
    end_date           = models.DateField( auto_now=False, auto_now_add=False)
    level_statues      = models.BooleanField()
    
    



