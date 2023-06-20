from django.shortcuts import render
from .models import Subject , Lesson
from .serializers import SubjectSerializer ,LessonSerializer
from rest_framework import generics
from Users.supervisor_permissions import CanEditSubject
# Create your views here.








# subject views

class CreateSubject(generics.CreateAPIView):
    queryset           = Subject.objects.all()
    serializer_class   = SubjectSerializer
    # permission_classes = [CanEditSubject]
    
    

class RetrieveSubject(generics.RetrieveAPIView):
    queryset           = Subject.objects.all()
    serializer_class   = SubjectSerializer
    permission_classes = [CanEditSubject]
    lookup_field       = 'subject_name'


class DeleteSubject(generics.DestroyAPIView):
    queryset           = Subject.objects.all()
    serializer_class   = SubjectSerializer
    permission_classes = [CanEditSubject]
    lookup_field       = 'subject_name'

class UpdateSubject(generics.RetrieveUpdateAPIView):
    queryset           = Subject.objects.all()
    serializer_class   = SubjectSerializer
    permission_classes = [CanEditSubject]
    lookup_field       = 'subject_name'
    


class ListSubject(generics.ListAPIView):
    queryset           = Subject.objects.all()
    serializer_class   = SubjectSerializer
    # permission_classes = [CanEditSubject]
    



# lesson views

class CreateLesson(generics.CreateAPIView):
    queryset           = Lesson.objects.all()
    serializer_class   = LessonSerializer
    permission_classes = [CanEditSubject]
    lookup_field       = 'lesson_name'
    

class RetrieveLesson(generics.RetrieveAPIView):
    queryset           = Lesson.objects.all()
    serializer_class   = LessonSerializer
    permission_classes = [CanEditSubject]
    lookup_field       = 'lesson_name'


class DeleteLesson(generics.DestroyAPIView):
    queryset           = Lesson.objects.all()
    serializer_class   = LessonSerializer
    permission_classes = [CanEditSubject]
    lookup_field       = 'lesson_name'

class UpdateLesson(generics.RetrieveUpdateAPIView):
    queryset           = Lesson.objects.all()
    serializer_class   = LessonSerializer
    permission_classes = [CanEditSubject]
    lookup_field       = 'lesson_name'





 
create_subject   = CreateSubject.as_view()
update_subject   = UpdateSubject.as_view()
delete_subject   = DeleteSubject.as_view()
retrieve_subject = RetrieveSubject.as_view()
list_subject     = ListSubject.as_view()




   
create_lesson   = CreateLesson.as_view()
update_lesson   = UpdateLesson.as_view()
delete_lesson   = DeleteLesson.as_view()
retrieve_lesson = RetrieveLesson.as_view()