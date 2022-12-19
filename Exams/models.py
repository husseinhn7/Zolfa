from django.db import models

# Create your models here.




class Exam(models.Model):
    title         = models.TextField(null=True , default= None)
    exam_creator  = models.ForeignKey("Users.User", on_delete=models.CASCADE ,null=True , default= None)
    start_date    = models.DateField( auto_now=False, auto_now_add=False , default=None)
    end_date      = models.DateField( auto_now=False, auto_now_add=False , default=None)
    exam_duration = models.IntegerField(null=True , default= None)
    final         = models.BooleanField(default=False , null=True )
    subj          = models.ForeignKey("Levels.Subject",  on_delete=models.CASCADE ,null=True , default= None)
    comment       = models.TextField(null=True , default= None)
    final_mark    = models.IntegerField(null=True , default= None)
    
    



class Question(models.Model):
    exam     = models.ForeignKey(Exam,  on_delete=models.CASCADE ,null=True , default= None)
    question = models.TextField(null=True , default= None)
    mark     = models.IntegerField(null=True , default= None)




class Options(models.Model):
    option   = models.TextField(null=True , default= None)
    question = models.ForeignKey(Question,  on_delete=models.CASCADE ,null=True , default= None)
    
    
    
    
    
    
class Marks(models.Model):
    student  = models.ForeignKey("Users.User",  on_delete=models.CASCADE ,null=True , default= None)
    exam     = models.ForeignKey(Exam, on_delete=models.CASCADE ,null=True , default= None)
    mark     = models.IntegerField(null=True , default= None)
    
    
    
class Answers(models.Model):
    student  = models.ForeignKey("Users.User",  on_delete=models.CASCADE ,null=True , default= None)
    exam     = models.ForeignKey(Exam,  on_delete=models.CASCADE ,null=True , default= None)
    question = models.ForeignKey(Question,  on_delete=models.CASCADE ,null=True , default= None)
    answer   = models.TextField(null=True , default= None)







