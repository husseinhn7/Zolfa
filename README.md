users/signup/   
users/login/    
users/logout/
users/create/   


# intake urls
users/update-intake/<str:name>/   update_intake 
users/create-intake/<str:name>/   create_intake 
users/delete-intake/<str:name>/   delete_intake 
users/retrieve-intake/<str:name>/   retrieve_intake 


# students urls 
users/update-student/<str:name>/     update_Student 
users/delete-student/<str:name>/     delete_Student 
users/retrieve-student/<int:pk>/     retrieve_Student 








levels/create-level/                                 create_level  
levels/update-level/<str:level_name>/                update_level  
levels/delete-level/<str:level_name>/                delete_level  
levels/retrieve-level/<str:level_name>/              retrieve_level  
# 
levels/create-subject/                               create_subject  
levels/update-subject/<str:subject_name>/            update_subject  
levels/delete-subject/<str:subject_name>/            delete_subject  
levels/retrieve-subject/<str:subject_name>/          retrieve_subject  
# 
levels/create-lesson/                                create_lesson  
levels/update-lesson/<str:lesson_name>/              update_lesson  
levels/delete-lesson/<str:lesson_name>/              delete_lesson  
levels/retrieve-lesson/<str:lesson_name>/            retrieve_lesson  