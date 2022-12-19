from django.urls import path 
from .views import create_exam , create_question , create_option
urlpatterns = [
    path('create-exam/'     , create_exam) ,
    path('create-question/' , create_question) ,
    path('create-option/'   , create_option) ,
    
]
