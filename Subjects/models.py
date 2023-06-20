from django.db import models

# Create your models here.




class Subject(models.Model):
    subject_name  = models.CharField( max_length=100)
    tutor_name    = models.ForeignKey("Users.User",default=None, on_delete=models.CASCADE)
    subject_level = models.ForeignKey("Levels.Level", default=None , on_delete=models.CASCADE)
    exams         = models.ForeignKey("Exams.Exam",  default=None , on_delete=models.CASCADE)
    
    




class Lesson(models.Model):
    lesson_name        = models.CharField( max_length=100 , null=True , default= None)
    lesson_description = models.TextField()
    lesson_pdf         = models.URLField( max_length=200)
    lesson_video       = models.URLField( max_length=200)
    subject            = models.ForeignKey(Subject,  default=None , on_delete=models.CASCADE)