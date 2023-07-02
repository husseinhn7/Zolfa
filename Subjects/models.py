from django.db import models

# Create your models here.




class Subject(models.Model):
    name  = models.CharField( max_length=100)
    level = models.ForeignKey("Levels.Level", default=None , on_delete=models.CASCADE)
    
    




class Lesson(models.Model):
    name               = models.CharField( max_length=100 , null=True , default= None)
    lesson_description = models.TextField()
    lesson_pdf         = models.URLField( max_length=200)
    lesson_video       = models.URLField( max_length=200)
    subject            = models.ForeignKey(Subject,  default=None , on_delete=models.CASCADE)