from Users.supervisor_permissions import  CanEditLevel
from rest_framework import generics 
from .models import Level  
from .serializers import LevelSerializer 
# Create your views here.

# level  views

class CreateLevel(generics.CreateAPIView):
    queryset           = Level.objects.all()
    serializer_class   = LevelSerializer
    # permission_classes = [CanEditLevel]

class RetrieveLevel(generics.RetrieveAPIView):
    queryset           = Level.objects.all()
    serializer_class   = LevelSerializer
    # permission_classes = [CanEditLevel]
    lookup_field       = 'name'



class DeleteLevel(generics.DestroyAPIView):
    queryset           = Level.objects.all()
    serializer_class   = LevelSerializer
    # permission_classes = [CanEditLevel]
    lookup_field       = 'name'

class UpdateLevel(generics.RetrieveUpdateAPIView):
    queryset           = Level.objects.all()
    serializer_class   = LevelSerializer
    # permission_classes = [CanEditLevel]
    lookup_field       = 'name'
    
    

class ListLevel(generics.ListAPIView):
    queryset           = Level.objects.all()
    serializer_class   = LevelSerializer
    # permission_classes = [CanEditLevel]
    







    
    
    
    
    
    
create_level   = CreateLevel.as_view()
update_level   = UpdateLevel.as_view()
delete_level   = DeleteLevel.as_view()
retrieve_level = RetrieveLevel.as_view()
list_levels    = ListLevel.as_view()



  

