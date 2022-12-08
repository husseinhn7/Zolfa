from django.db import models
from Users.models import User
from Exams.models import Exam

# Create your models here.


class Level(models.Model):
    level_name         = models.CharField( max_length=100)
    number_of_students = models.IntegerField()
    start_date         = models.DateField( auto_now=False, auto_now_add=False)
    end_date           = models.DateField( auto_now=False, auto_now_add=False)
    level_statues      = models.BooleanField()
    
    





class Subject(models.Model):
    subject_name  = models.CharField( max_length=100)
    tutor_name    = models.ForeignKey(User,default=None, on_delete=models.CASCADE)
    subject_level = models.ForeignKey(Level, default=None , on_delete=models.CASCADE)
    exams         = models.ForeignKey(Exam,  default=None , on_delete=models.CASCADE)
    
    




class Lesson(models.Model):
    lesson_name        = models.CharField( max_length=100 , null=True , default= None)
    lesson_description = models.TextField()
    lesson_pdf         = models.URLField( max_length=200)
    lesson_video       = models.URLField( max_length=200)
    subject            = models.ForeignKey(Subject,  default=None , on_delete=models.CASCADE)