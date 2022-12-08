from .models import User
from .serializers import StudentSerializer
from rest_framework import generics
from .supervisor_permissions import  CanEditStudentsData

   

    
    
class DeleteStudent(generics.DestroyAPIView):
    serializer_class = StudentSerializer
    permission_classes   = [  CanEditStudentsData ]
    lookup_field     = 'name'
    
    def get_queryset(self):
        objects  = User.objects.all()
        query    = objects.filter( is_staff = False)
        return query
    
    



class UpdateStudent( generics.RetrieveUpdateAPIView):
    queryset         = User.objects.all()
    serializer_class = StudentSerializer
    permission_classes   = [  CanEditStudentsData ]
    lookup_field     = 'name'
    
    
    def get_queryset(self):
        objects  = User.objects.all()
        query    = objects.filter( is_staff = False)
        return query
    
    
   
    

class RetrieveStudent(generics.RetrieveAPIView):
    queryset         = User.objects.all()
    serializer_class = StudentSerializer
    permission_classes   = [  CanEditStudentsData ]
    lookup_field     = 'pk'
    
    
    def get_queryset(self):
        objects  = User.objects.all()
        query    = objects.filter( is_staff = False)
        return query
    
    
    
    
    
    
    
update_Student   = UpdateStudent.as_view()
delete_Student   = DeleteStudent.as_view()
retrieve_Student = RetrieveStudent.as_view()


    
    
    
    