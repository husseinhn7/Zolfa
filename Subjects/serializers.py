from rest_framework import serializers
from .models import Subject , Lesson
class SubjectSerializer(serializers.ModelSerializer):
    pk = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model  = Subject
        fields = [
            'pk' ,
            'name',
            'level',
        ]
        
        

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Lesson
        fields = [
            'name',
            'lesson_description',
            'lesson_pdf',
            'lesson_video',
            'subject',
        ]
        
        
        
        
