from rest_framework import serializers
from .models import Exam , Question , Options , Answers , Marks 
from Levels.models import Subject



class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Options
        fields = [
            'option',
            'question',
            'correct_option',
            'final_mark'
        ]
    

class QuestionSerializer(serializers.ModelSerializer):
    # op = OptionSerializer()
    class Meta:
        model  = Question
        fields = [
            'exam',
            'question',
            'mark',
            # 'op',
        ]

    


class ExamSerializer(serializers.ModelSerializer):
    # qus = QuestionSerializer()
    class Meta:
        model  = Exam
        fields = [
            # 'qus',
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
    
    
    
    
    
    
    
    
    
class AnswerSerializer(serializers.ModelSerializer):
    exam = serializers.CharField(max_length= 400)
    class Meta:
        model  = Answers
        fields = [
            'answer' ,
            'question' ,
            'exam'
        ]
        
    def create(self, validated_data):
        Answer          = Answers(answer=validated_data['answer'])
        Answer.student  = self.context['request'].user
        Answer.question = Question.objects.get(question=validated_data['question'])
        option = Options.objects.get(option=validated_data['answer'])
        mark = Marks.objects.get(student = Answer.student , exam = validated_data['exam'] )
        if option.correct_option:
            mark.mark  = mark.final_mark + mark.mark 
            mark.save()
        
        return mark
    
    
    
class MarkSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Marks
        fields =[
            'exam',
        ]
        
    def create(self, validated_data):
        mark         = Marks(**validated_data)
        mark.student = self.context['request'].user
        mark.mark    = 0
        mark.save()
        return mark