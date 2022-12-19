from rest_framework import serializers
from .models import Exam , Question , Options
from Levels.models import Subject




class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Exam
        fields = [
            'title',
            'start_date',
            'end_date',
            'exam_duration',
            'final',
            'subj',
            'comment',
            'final_mark',
        ]
        
        
    def create(self, validated_data):
        exam              = Exam(**validated_data)
        subj              = Subject.objects.filter(subject_name=validated_data['subj']).first()
        exam.exam_creator = self.context['request'].user
        exam.subj         = subj
        exam.save()
        # print(self.request)
        return exam
    
    
    
    
    
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Question
        fields = [
            'exam',
            'question',
            'mark',
        ]

    
    
    
    
    

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Options
        fields = [
            'option',
            'question',
        ]
    