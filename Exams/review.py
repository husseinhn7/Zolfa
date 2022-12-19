from .models import Options , Exam , Answers , Marks 
from Users.models import User



class Review:
    def Check_answer(self):
        ans = Answers.objects.get()
        cor = Options.objects.get( correct_option= True)
        if cor.option  == ans:
            mark = Marks( student =0   , exam = 0  , mark=0  ) 
            mark.save()
    def __init__(self , student : User , ) :
        pass