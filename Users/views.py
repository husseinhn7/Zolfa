from django.shortcuts import render
from rest_framework import generics , permissions 
from rest_framework.response import Response
from .supervisor_permissions import CanEditIntakeData , CanEditExam
from rest_framework.views import APIView
from django.contrib.auth import login , logout , authenticate
from .models import User 
from .serializers import StudentSerializer , SupervisorSerializer 
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
