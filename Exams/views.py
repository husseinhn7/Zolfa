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







class StartExam(generics.RetrieveAPIView):
    queryset         = Marks.objects.all()
    serializer_class =  MarkSerializer
    
    
    def get(self, request, *args, **kwargs):
        exam_id = self.kwargs.get('exam')
        student_id = self.kwargs.get('student') 
        query = Marks.objects.filter(exam = exam_id , student = student_id)
        if query.exists() :
            mark = MarkSerializer(query.first()).data
            return Response(mark)
        else :
            data = {'exam' : exam_id , 'student' : student_id , 'mark' : 0}
            serializer = MarkSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            mark = serializer.save()
        return Response({ 'status' : True , **data , 'id' : mark.pk })
        
        
        
        
    
    
    



class Answer(generics.CreateAPIView):
    queryset         = Answers.objects.all()
    serializer_class = AnswerSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = AnswerSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        optionPk = request.data['answer']
        option = Options.objects.get(pk=optionPk )
        markPk = self.kwargs.get('markPk')
        if option.correct_option:
            mark = Marks.objects.get(pk = markPk)
            mark.mark  = mark.mark + 10
            mark.save()
        return Response(serializer.data , status=201 )
    
    
    
    
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



class RetrieveMark(generics.RetrieveAPIView):
    queryset         = Marks.objects.all()
    serializer_class =  MarkSerializer
    
    def get(self, request, *args, **kwargs):
        examPk = self.kwargs.get('pk')
        studentPk =  self.kwargs.get('pm')
        query = Marks.objects.filter(exam = examPk , student = studentPk)
        if query.exists() :
            mark = MarkSerializer(query.first()).data
            return Response(mark)
        return Response({ 'status' : True})



create_exam     = CreateExam.as_view()
create_question = CreateQuestion.as_view()
create_option   = CreateOption.as_view()

retrieve_exam     = RetrieveExam.as_view()
retrieve_question = RetrieveQuestion.as_view()
retrieve_option   = RetrieveOptions.as_view()


answer          = Answer.as_view()
start_exam      = StartExam.as_view()
retrieve_mark   = RetrieveMark.as_view()
