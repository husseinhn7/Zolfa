from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.




    
    
class User(AbstractUser):
    name                 = models.CharField( max_length=50)
    age                  = models.IntegerField( null= True)
    username             = models.CharField( max_length=11 , unique=True)
    password             = models.CharField( max_length=100) 
    gender               = models.CharField( max_length=20)
    education            = models.CharField( max_length=70 , null= True)
    register_date        = models.DateField( auto_now=True, auto_now_add=False )
    courses              = models.BooleanField(default= False ,   null= True)
    courses_description  = models.TextField ( default=None , null = True)
    level                = models.ForeignKey('Levels.Level' ,default=None, on_delete=models.CASCADE , null= True)
    intake               = models.ForeignKey('Intakes.Intake',default=None, on_delete=models.CASCADE , null= True)
    is_staff             = models.BooleanField(default=False , null=True)
    
class Permissions(models.Model):
    supervisor                  = models.ForeignKey("Users.User", null=True ,  on_delete=models.CASCADE)
    can_edit_levels             = models.BooleanField(default=False , null=True)
    see_intake_level_statistics = models.BooleanField(default=False , null=True)
    can_edit_users_data         = models.BooleanField(default=False , null=True)
    can_edit_exam_results       = models.BooleanField(default=False , null=True)
    can_edit_exam               = models.BooleanField(default=False , null=True)
    can_edit_subject            = models.BooleanField(default=False , null=True)
    can_edit_level              = models.BooleanField(default=False , null=True)
    
    def __str__(self):
        return f"permissions of {self.supervisor}"
    




