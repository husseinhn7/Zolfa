from rest_framework import serializers
from .models import Level 




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
        
        
        
