from django.db import models

# Create your models here.





class Intake(models.Model):
    name                 = models.CharField( max_length=100)
    level                = models.ForeignKey('Levels.Level' , null=True, default=None , on_delete=models.CASCADE)
    intake_description   = models.TextField()
    start_date           = models.DateField( auto_now=True, auto_now_add=False)
    register_date        = models.DateField( auto_now=False, auto_now_add=False)
    expire_date          = models.DateField( auto_now=False, auto_now_add=False)
    telegram_link_men    = models.URLField( max_length=200)
    telegram_link_women  = models.URLField( max_length=200)
    