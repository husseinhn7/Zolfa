from rest_framework import generics 
import json
from rest_framework.response import Response
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
    
    
    
    
class RetrieveExam(generics.RetrieveAPIView):
    serializer_class = ExamSerializer
    
    def get_queryset(self):
        exam_id = self.kwargs.get('pk')
        query       = Exam.objects.filter(pk=exam_id)
        return query
    

class RetrieveQuestion(generics.ListAPIView):
    serializer_class = QuestionSerializer
    
    def get_queryset(self):
        exam_id = self.kwargs.get('pk')
        query       = Question.objects.filter(exam=exam_id)
        return query
    
    def get(self, request, *args, **kwargs):
        exam_id = self.kwargs.get('pk')
        query  = Question.objects.filter(exam=exam_id)
        data = []
        for i in query:
            op = Options.objects.filter(question = i.pk)
            data.append({'question' : QuestionSerializer(i).data , 'option' : [OptionSerializer(x).data for x in op]})
            
        
        return Response(data)
    
class RetrieveOptions(generics.ListAPIView):
    serializer_class = OptionSerializer
    
    def get_queryset(self):
        question_id = self.kwargs.get('pk')
        query       = Options.objects.filter(question=question_id)
        return query

create_exam     = CreateExam.as_view()
create_question = CreateQuestion.as_view()
create_option   = CreateOption.as_view()

retrieve_exam     = RetrieveExam.as_view()
retrieve_question = RetrieveQuestion.as_view()
retrieve_option   = RetrieveOptions.as_view()


answer          = Answer.as_view()
start_exam      = StartExam.as_view()
