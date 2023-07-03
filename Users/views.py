from django.shortcuts import render
from rest_framework import generics , permissions 
from rest_framework.response import Response
from .supervisor_permissions import CanEditIntakeData , CanEditExam
from rest_framework.views import APIView
from django.contrib.auth import login , logout , authenticate
from .models import User , Permissions
from .serializers import StudentSerializer , SupervisorSerializer , StudentNameSerializer , PermissionsSerializer
# Create your views here.


class StudentSignup(generics.CreateAPIView):
    queryset         = User.objects.all()
    serializer_class = StudentSerializer


class StudentLogin(generics.CreateAPIView):
    queryset         = User.objects.all()
    serializer_class = StudentSerializer
    
    
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user=authenticate(request , username = username , password = password)
        print(request)
        print(username)
        print(request.data)
        print(password)
        if user!=None:
            print(request)
            login(request,user)
            return Response({'msg':'user logged in successfully','user' : f"{user}"})
        return Response({'msg':'this user does not exists' ,'user' : f"{user}"})

class StudentLogout(APIView):
    queryset           = User.objects.all()
    serializer_class   = StudentSerializer
    permission_classes = [ permissions.IsAuthenticated ]
    
    def get(self, request):
        user = request.user
        logout(request)
        return Response({'msg':'user logged out successfully', 'msg 2' : f'{user}' ,'user' : f"{request.user}"} )
        
        




class CreateSupervisor(generics.CreateAPIView):
    queryset           = User.objects.all()
    serializer_class   = SupervisorSerializer




class ListSupervisor(generics.ListAPIView):
    serializer_class = SupervisorSerializer
    
    def get_queryset(self):
        permission = self.kwargs.get('per')
        print(permission)
        return User.objects.filter(**{f'permissions__{permission}' : True})






class RetrieveStudentName(generics.RetrieveAPIView):
    queryset         = User.objects.all()
    serializer_class = StudentNameSerializer
    lookup_field     = 'name'
    
    


class AddSupervisor(generics.CreateAPIView):
    queryset = Permissions.objects.all()
    serializer_class = PermissionsSerializer
    

class UpdateSupervisor(generics.UpdateAPIView):
    queryset = Permissions.objects.all()
    serializer_class = PermissionsSerializer
    lookup_field = 'name'
class DeleteSupervisor(generics.DestroyAPIView):
    queryset = Permissions.objects.all()
    serializer_class = PermissionsSerializer
    lookup_field = 'name'

class RetrieveSupervisor(generics.RetrieveAPIView):
    
    def get(self, request, *args, **kwargs):
        name = self.kwargs.get('name')
        user = User.objects.filter(name = name).first()
        if not user:
            return Response({'m':'user do' } , status=404)
        permissions = Permissions.objects.filter(supervisor = user).first()
        if not permissions:
            return Response({'m':'user do' } , status=404)
        # print(permissions)
        Json_permissions = PermissionsSerializer(permissions).data
        return Response(Json_permissions)








update_supervisor = UpdateSupervisor.as_view()
delete_supervisor = DeleteSupervisor.as_view()
get_supervisor_permissions = RetrieveSupervisor.as_view()

add_supervisor = AddSupervisor.as_view()
get_student = RetrieveStudentName.as_view()




list_supervisor = ListSupervisor.as_view()
























Student_Signup_view    = StudentSignup.as_view()
Student_login_view     = StudentLogin.as_view()
Student_logout_view    = StudentLogout.as_view()






create_supervisor_view = CreateSupervisor.as_view()







class test(APIView):
    # parser_classes = 
    permission_classes =[CanEditIntakeData]
    def get(self , request):
        user = User.objects.get(username='')
        prem = user.permissions_set.first()
        ote  = prem.can_edit_levels
        return Response({'msg' : f'{ote}'})
    
t = test.as_view()
