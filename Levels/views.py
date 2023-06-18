from Users.supervisor_permissions import CanEditSubject , CanEditLevel
from rest_framework import generics 
from .models import Level  , Subject , Lesson
from .serilaizers import LevelSerializer , SubjectSerializer , LessonSerializer
# Create your views here.

# level  views

class CreateLevel(generics.CreateAPIView):
    queryset           = Level.objects.all()
    serializer_class   = LevelSerializer
    permission_classes = [CanEditLevel]


class RetrieveLevel(generics.RetrieveAPIView):
    queryset           = Level.objects.all()
    serializer_class   = LevelSerializer
    permission_classes = [CanEditLevel]
    lookup_field       = 'level_name'



class DeleteLevel(generics.DestroyAPIView):
    queryset           = Level.objects.all()
    serializer_class   = LevelSerializer
    permission_classes = [CanEditLevel]
    lookup_field       = 'level_name'

class UpdateLevel(generics.RetrieveUpdateAPIView):
    queryset           = Level.objects.all()
    serializer_class   = LevelSerializer
    permission_classes = [CanEditLevel]
    lookup_field       = 'level_name'








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
    
    
    
    
    
    
create_level   = CreateLevel.as_view()
update_level   = UpdateLevel.as_view()
delete_level   = DeleteLevel.as_view()
retrieve_level = RetrieveLevel.as_view()



   
create_subject   = CreateSubject.as_view()
update_subject   = UpdateSubject.as_view()
delete_subject   = DeleteSubject.as_view()
retrieve_subject = RetrieveSubject.as_view()
list_subject     = ListSubject.as_view()




   
create_lesson   = CreateLesson.as_view()
update_lesson   = UpdateLesson.as_view()
delete_lesson   = DeleteLesson.as_view()
retrieve_lesson = RetrieveLesson.as_view()

