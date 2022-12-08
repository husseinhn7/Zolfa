from .models import Intake
from .serializers import IntakeSerializer
from rest_framework import generics
from .supervisor_permissions import CanEditIntakeData

   


class CreateIntake(generics.CreateAPIView):
    queryset         = Intake.objects.all()
    serializer_class = IntakeSerializer
    permission_classes   = [ CanEditIntakeData ]
    
    
    
    
class DeleteIntake(generics.DestroyAPIView):
    queryset         = Intake.objects.all()
    serializer_class = IntakeSerializer
    permission_classes   = [ CanEditIntakeData ]
    lookup_field     = 'name'
    
    



class UpdateIntake( generics.RetrieveUpdateAPIView):
    queryset         = Intake.objects.all()
    serializer_class = IntakeSerializer
    permission_classes   = [ CanEditIntakeData ]
    lookup_field     = 'name'
    
   
    

class RetrieveIntake(generics.RetrieveAPIView):
    queryset         = Intake.objects.all()
    serializer_class = IntakeSerializer
    permission_classes   = [ CanEditIntakeData ]
    lookup_field     = 'name'
    
    
    
    
    
    
create_intake   = CreateIntake.as_view()
update_intake   = UpdateIntake.as_view()
delete_intake   = DeleteIntake.as_view()
retrieve_intake = RetrieveIntake.as_view()


    
    
    
    