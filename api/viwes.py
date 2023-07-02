from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from Users.models import User , Permissions

'''
can_edit_levels             = models.BooleanField(default=False , null=True)
see_intake_level_statistics = models.BooleanField(default=False , null=True)
can_edit_users_data         = models.BooleanField(default=False , null=True)
can_edit_exam_results       = models.BooleanField(default=False , null=True)
can_edit_exam               = models.BooleanField(default=False , null=True)
can_edit_subject            = models.BooleanField(default=False , null=True)
can_edit_level
'''
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    permission_classes = ()
    @classmethod
    def get_token(cls, user : User):
        token = super().get_token(user)
        if user.is_staff : 
            permissions = Permissions.objects.get(supervisor = user.pk)
            token['can_edit_levels'] = permissions.can_edit_levels
            token['see_intake_level_statistics'] = permissions.see_intake_level_statistics
            token['can_edit_users_data'] = permissions.can_edit_users_data
            token['can_edit_exam_results'] = permissions.can_edit_exam_results
            token['can_edit_exam'] = permissions.can_edit_exam
            token['can_edit_subject'] = permissions.can_edit_subject
            token['can_edit_level'] = permissions.can_edit_level
            token['name'] = user.name
            token['is_staff'] = user.is_staff 

        # Add custom claims
        token['name'] = user.name
        token['is_staff'] = user.is_staff 
        # ...
        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer