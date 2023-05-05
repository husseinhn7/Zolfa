from django.urls import path 
from .views import create_exam , create_question , create_option , start_exam , answer ,retrieve_exam , retrieve_option ,retrieve_question
urlpatterns = [
    path('create-exam/'     , create_exam) ,
    path('create-question/' , create_question) ,
    path('create-option/'   , create_option) ,
    path('start-exam/'      , start_exam) ,
    
    path('retrieve-exam/<int:pk>'      , retrieve_exam) ,
    path('retrieve-questions/<int:pk>'      , retrieve_question) ,
    path('retrieve-options/<int:pk>'      , retrieve_option) ,
    
    path('answer-exam/'     , answer) ,

    
]
