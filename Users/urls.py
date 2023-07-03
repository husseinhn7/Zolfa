from django.urls import path 
from .views import ( 
                    Student_Signup_view ,
                    Student_login_view  , 
                    Student_logout_view , 
                    t ,
                    create_supervisor_view ,
                    list_supervisor , 
                    get_student,
                    add_supervisor , 
                    get_supervisor_permissions , 
                    delete_supervisor,
                    update_supervisor ,
 )
from .student_views import update_Student , delete_Student , retrieve_Student

urlpatterns = [
    path( 'signup/' , Student_Signup_view ) , 
    path( 'login/'  ,  Student_login_view ) ,
    path( 'logout/' , Student_logout_view  ) ,
    path( 'create/' , create_supervisor_view ) ,
    path( 'list-supervisor/<str:per>/' , list_supervisor ) ,
    path('add-supervisor/' , add_supervisor ) ,
    path( 't/' , t ) ,
    path( 'get-supervisor/<str:name>/' , get_supervisor_permissions ) ,
    path( 'delete-supervisor/<str:name>/' , delete_supervisor ) ,
    path( 'update-supervisor/<str:name>/' , update_supervisor ) ,
    # students urls 
    path( 'update-student/<str:name>/' , update_Student ) ,
    path( 'delete-student/<str:name>/' , delete_Student ) ,
    path( 'retrieve-student/<str:name>/' , retrieve_Student ) ,
    path( 'retrieve-student-pk/<str:name>/' , get_student ) ,
    
]
