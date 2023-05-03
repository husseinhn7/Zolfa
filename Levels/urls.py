from django.urls import path 
from .views import (
                    create_level ,
                    update_level ,
                    delete_level , 
                    retrieve_level , 
                    
                    create_lesson , 
                    update_lesson , 
                    delete_lesson , 
                    retrieve_lesson ,
                    
                    create_subject ,
                    update_subject ,
                    delete_subject , 
                    retrieve_subject ,
                    list_subject
)


urlpatterns = [
    # 
    path('create-level/' , create_level) , 
    path('update-level/<str:level_name>/' , update_level) , 
    path('delete-level/<str:level_name>/' , delete_level) , 
    path('retrieve-level/<str:level_name>/' , retrieve_level) , 
    # 
    path('create-subject/' , create_subject) , 
    path('update-subject/<str:subject_name>/' , update_subject) , 
    path('delete-subject/<str:subject_name>/' , delete_subject) , 
    path('retrieve-subject/<str:subject_name>/' , retrieve_subject) , 
    path('list-subjects' , list_subject) , 
    # 
    path('create-lesson/' , create_lesson) , 
    path('update-lesson/<str:lesson_name>/' , update_lesson) , 
    path('delete-lesson/<str:lesson_name>/' , delete_lesson) , 
    path('retrieve-lesson/<str:lesson_name>/' , retrieve_lesson) , 
    
    
]
