from django.db import models

# Create your models here.




class Exam(models.Model):
    exam_creator  = models.ForeignKey("Users.User", on_delete=models.CASCADE)
    start_date    = models.DateField( auto_now=False, auto_now_add=False)
    end_date      = models.DateField( auto_now=False, auto_now_add=False)
    exam_duration = models.IntegerField()
    final         = models.BooleanField()
    subject       = models.ForeignKey("Levels.Subject",  on_delete=models.CASCADE)
    comment       = models.TextField(null=True , default= None)
    
    



class Question(models.Model):
    exam     = models.ForeignKey(Exam,  on_delete=models.CASCADE)
    question = models.ForeignKey("app.Model",  on_delete=models.CASCADE)
    mark     = models.IntegerField()




class Options(models.Model):
    option   = models.TextField()
    question = models.ForeignKey(Question,  on_delete=models.CASCADE)
    
    
    
    
    
    
class Marks(models.Model):
    student  = models.ForeignKey("Users.User",  on_delete=models.CASCADE)
    exam     = models.ForeignKey(Exam, on_delete=models.CASCADE)
    mark     = models.IntegerField()
    
    
    
class Answers(models.Model):
    pass







