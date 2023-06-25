from django.urls import path 
from .views import update_intake , create_intake , delete_intake , retrieve_intake



urlpatterns = [
    # intake urls
    path( 'update-intake/<int:pk>/'     , update_intake ) ,
    path( 'create-intake/'              , create_intake ) ,
    path( 'delete-intake/<int:pk>/'     , delete_intake ) ,
    path( 'retrieve-intake/<str:name>/' , retrieve_intake ) ,
]
