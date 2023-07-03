from rest_framework import serializers              
from .models import User  ,  Permissions  
from Levels.models import Level


    
 
    
class PermissionsSerializer(serializers.ModelSerializer):
    class Meta :
        model  = Permissions
        fields = [
            'supervisor',
            'name',
            'can_edit_levels',
            'see_statistics',
            'can_edit_users_data',
            'can_edit_exam_results',
            'can_edit_exam',
            'can_edit_subject',
            'can_edit_intakes',
            'can_edit_landing_page'      
        ]
    def create(self, validated_data):
        user = validated_data['supervisor'] 
        
        user.is_staff = True
        user.save()
        permission = Permissions(**validated_data)
        permission.name = user.name
        permission.save()
        return permission
    
    

class SupervisorSerializer(serializers.ModelSerializer):
    permissions_set = PermissionsSerializer(many=True, read_only=True)
    # permissions_related_field = serializers.BooleanField(source='permissions.can_edit_exam')

    class Meta:
        model  = User
        fields = [
            # supervisor fields 
            'name',
            'age',
            'username',
            'gender',
            'is_staff',
            'permissions_set' 
        ]
    def get_fields(self):
        
        return super().get_fields()
    
    
    
   
        
class StudentSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

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
        
        
class StudentNameSerializer(serializers.ModelSerializer):
    pk = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = User
        fields = [
            'pk' , 
            'name'
            ]