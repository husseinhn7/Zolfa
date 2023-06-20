from rest_framework import serializers
from .models import Intake


 
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
        
        