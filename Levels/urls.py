from django.urls import path 
from .views import (
                    create_level ,
                    update_level ,
                    delete_level , 
                    retrieve_level , 
                    list_levels ,
                    
                 
)


urlpatterns = [
    # 
    path('create-level/' , create_level) , 
    path('update-level/<str:name>/' , update_level) , 
    path('delete-level/<str:name>/' , delete_level) , 
    path('retrieve-level/<str:name>/' , retrieve_level) , 
    path('list-levels/' , list_levels) , 
    # 
   
    
]
