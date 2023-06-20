from rest_framework import serializers
from .models import Subject , Lesson
class SubjectSerializer(serializers.ModelSerializer):
    pk = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model  = Subject
        fields = [
            'pk' ,
            'subject_name',
            'tutor_name',
            'subject_level',
            'exams',
        ]
        
        

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Lesson
        fields = [
            'lesson_name',
            'lesson_description',
            'lesson_pdf',
            'lesson_video',
            'subject',
        ]
        
        
        
        
