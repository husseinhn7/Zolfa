from django.urls import path 
from .views import ( 
                    Student_Signup_view ,
                    Student_login_view  , 
                    Student_logout_view , 
                    t ,
                    create_supervisor_view ,
                    list_supervisor , 
 )
from .student_views import update_Student , delete_Student , retrieve_Student

urlpatterns = [
    path( 'signup/' , Student_Signup_view ) , 
    path( 'login/'  ,  Student_login_view ) ,
    path( 'logout/' , Student_logout_view  ) ,
    path( 'create/' , create_supervisor_view ) ,
    path( 'list-supervisor/<str:per>/' , list_supervisor ) ,

    path( 't/' , t ) ,
    
    # students urls 
    path( 'update-student/<str:name>/' , update_Student ) ,
    path( 'delete-student/<str:name>/' , delete_Student ) ,
    path( 'retrieve-student/<int:pk>/' , retrieve_Student ) ,


]
