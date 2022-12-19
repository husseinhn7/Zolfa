from django.shortcuts import render
from rest_framework import generics
from .models import Exam , Question , Options
from .exam_serializers import ExamSerializer , QuestionSerializer , OptionSerializer
from Users.supervisor_permissions import CanEditExam
# Create your views here.


class CreateExam(generics.CreateAPIView):
    queryset           = Exam.objects.all()
    serializer_class   = ExamSerializer
    # permission_classes = [CanEditExam]
    


class CreateQuestion(generics.CreateAPIView):
    queryset           = Question.objects.all()
    serializer_class   = QuestionSerializer




class CreateOption(generics.CreateAPIView):
    queryset         = Options.objects.all()
    serializer_class = OptionSerializer









create_exam     = CreateExam.as_view()
create_question = CreateQuestion.as_view()
create_option   = CreateOption.as_view()