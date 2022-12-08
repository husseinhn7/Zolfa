from django.urls import path 
from .views import ( 
                    Student_Signup_view ,
                    Student_login_view  , 
                    Student_logout_view , 
                    t ,
                    create_supervisor_view ,
 )
from .intake_views import update_intake , create_intake , delete_intake , retrieve_intake
from .student_views import update_Student , delete_Student , retrieve_Student

urlpatterns = [
    path( 'signup/' , Student_Signup_view ) , 
    path( 'login/'  ,  Student_login_view ) ,
    path( 'logout/' , Student_logout_view  ) ,
    path( 'create/' , create_supervisor_view ) ,
    path( 't/' , t ) ,
    # intake urls
    path( 'update-intake/<str:name>/'   , update_intake ) ,
    path( 'create-intake/<str:name>/'   , create_intake ) ,
    path( 'delete-intake/<str:name>/'   , delete_intake ) ,
    path( 'retrieve-intake/<str:name>/' , retrieve_intake ) ,
    # students urls 
    path( 'update-student/<str:name>/' , update_Student ) ,
    path( 'delete-student/<str:name>/' , delete_Student ) ,
    path( 'retrieve-student/<int:pk>/' , retrieve_Student ) ,


]
