from rest_framework import generics
from .models import Exam , Question , Options , Marks , Answers
from .exam_serializers import ExamSerializer , QuestionSerializer , OptionSerializer , MarkSerializer , AnswerSerializer
from Users.supervisor_permissions import CanEditExam
# Create your views here.


class CreateExam(generics.CreateAPIView):
    queryset           = Exam.objects.all()
    serializer_class   = ExamSerializer
    # permission_classes = [CanEditExam]
    


class CreateQuestion(generics.CreateAPIView):
    queryset           = Question.objects.all()
    serializer_class   = QuestionSerializer
    # permission_classes = [CanEditExam]




class CreateOption(generics.CreateAPIView):
    queryset         = Options.objects.all()
    serializer_class = OptionSerializer
    # permission_classes = [CanEditExam]







class StartExam(generics.CreateAPIView):
    queryset         = Marks.objects.all()
    serializer_class =  MarkSerializer



class Answer(generics.CreateAPIView):
    queryset         = Answers.objects.all()
    serializer_class = AnswerSerializer
    



create_exam     = CreateExam.as_view()
create_question = CreateQuestion.as_view()
create_option   = CreateOption.as_view()
answer          = Answer.as_view()
start_exam      = StartExam.as_view()
