from rest_framework import serializers
from .models import Level , Lesson , Subject




class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Level
        fields = [
            'level_name',
            'number_of_students',
            'start_date',
            'end_date',
            'level_statues',
        ]
        
        
        

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Subject
        fields = [
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
        
        
        
        
