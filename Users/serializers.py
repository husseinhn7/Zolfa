from rest_framework import serializers              
from .models import User  ,  Permissions , Intake

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model  = User
        fields = [
            'name',
            'age',
            'username',
            'password',
            'gender',
            'education',
            'courses',
            'courses_description',
            'level',
            'intake',
        ]
    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    
    
    

class SupervisorSerializer(serializers.ModelSerializer):
    can_edit_levels             = serializers.BooleanField( default=False )
    see_intake_level_statistics = serializers.BooleanField( default=False )
    can_edit_users_data         = serializers.BooleanField( default=False )
    can_edit_exam_results       = serializers.BooleanField( default=False )
    can_edit_exam               = serializers.BooleanField( default=False )
    can_edit_subject            = serializers.BooleanField( default=False )
    can_edit_level              = serializers.BooleanField( default=False )
    class Meta:
        model  = User
        fields = [
            # supervisor fields 
            'name',
            'age',
            'username',
            'password',
            'gender',
            'is_staff',
            # permission fields 
            'can_edit_levels',
            'see_intake_level_statistics',
            'can_edit_users_data',
            'can_edit_exam_results',
            'can_edit_exam'
            
        ]
    def create(self, validated_data):
        
        user = User(
            name     = validated_data['name'] ,
            age      = validated_data['age'] ,
            username = validated_data['username'] ,
            gender   = validated_data['gender'] ,
            is_staff = validated_data['is_staff'] ,
            
        )
        user.set_password(validated_data['password'])
        user.save()
        if user.is_staff:
            permissions = Permissions (
                can_edit_levels             = validated_data['can_edit_levels'] ,
                see_intake_level_statistics = validated_data['see_intake_level_statistics'] ,
                can_edit_users_data         = validated_data['can_edit_users_data'], 
                can_edit_exam_results       = validated_data['can_edit_exam_results'], 
                can_edit_exam               = validated_data['can_edit_exam'], 
                can_edit_subject            = validated_data['can_edit_subject'],
                can_edit_level              = validated_data['can_edit_level'],
            )  
            permissions.supervisor = user 
            permissions.save()
            print(permissions)
            print(permissions.supervisor)
        return user
    
    
    
    
    
class IntakeSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Intake
        fields = [ 
                  'name' ,
                  'level',
                  'intake_description',
                  'start_date',
                  'register_date',
                  'expire_date',
                  'telegram_link_men',
                  'telegram_link_women',
                ]
        
        
        
        