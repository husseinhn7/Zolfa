from rest_framework import serializers
from .models import Level , Lesson , Subject




class LevelSerializer(serializers.ModelSerializer):
    pk = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model  = Level
        fields = [
            'pk', 
            'level_name',
            'number_of_students',
            'start_date',
            'end_date',
            'level_statues',
        ]
        
        
        

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
        
        
        
        
