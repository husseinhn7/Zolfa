from django.urls import path 
from .views import (
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
    path('create-subject/' , create_subject) , 
    path('update-subject/<str:name>/' , update_subject) , 
    path('delete-subject/<str:name>/' , delete_subject) , 
    path('retrieve-subject/<str:name>/' , retrieve_subject) , 
    path('list-subjects/' , list_subject) , 
    # 
    path('create-lesson/' , create_lesson) , 
    path('update-lesson/<str:name>/' , update_lesson) , 
    path('delete-lesson/<str:name>/' , delete_lesson) , 
    path('retrieve-lesson/<str:name>/' , retrieve_lesson) , 
    
]
