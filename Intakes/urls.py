from django.urls import path 
from .views import update_intake , create_intake , delete_intake , retrieve_intake



urlpatterns = [
    # intake urls
    path( 'update-intake/<str:name>/'     , update_intake ) ,
    path( 'create-intake/'              , create_intake ) ,
    path( 'delete-intake/<str:name>/'     , delete_intake ) ,
    path( 'retrieve-intake/<str:name>/' , retrieve_intake ) ,
]
