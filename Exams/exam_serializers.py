from rest_framework import serializers
from .models import Exam , Question , Options , Answers , Marks 



class OptionSerializer(serializers.ModelSerializer):
    pk = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        
        model  = Options
        
        fields = [
            'pk',  
            'option',
            'question',
            'correct_option',
            'final_mark'
        ]
        
        def create(self, validated_data):
            option = Options(**validated_data)
            option.question = Question.objects.filter( question = validated_data['question'] )
            option.save()
            return option 
    

class QuestionSerializer(serializers.ModelSerializer):
    # op = OptionSerializer()
    pk = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model  = Question
        fields = [
            'pk' ,
            'exam',
            'question',
            'mark',
            # 'op',
        ]
        
        # def create(self, validated_data):
        #     question = Question(**validated_data)
        #     question.exam = Exam.objects.filter( title = validated_data['exam'] )
        #     question.save()
        #     return question 

    


class ExamSerializer(serializers.ModelSerializer):
    # qus = QuestionSerializer()
    pk = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model  = Exam
        fields = [
            # 'qus',
            'pk',
            'exam_creator',
            'title', 
            'start_date',
            'end_date',
            'exam_duration',
            'final',
            'subj',
            'comment',
            'final_mark',
        ]
        
        
    
    
    
    
    
    
    
    
    
    
class AnswerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model  = Answers
        fields = [
            'student' ,
            'answer' ,
            'question' ,
            'exam'
        ]
        
    
    
    
    
class MarkSerializer(serializers.ModelSerializer):
    pk = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model  = Marks
        fields =[
            'pk' ,  
            'student',
            'exam',
            'mark'
            
        ]
        
  