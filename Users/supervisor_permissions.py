from rest_framework import permissions

class CanEditIntakeData(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            user             = request.user
            permission_model = user.permissions_set.first()
            permission       = permission_model.can_edit_levels
            return permission
        except AttributeError:
            return False


class CanEditStudentsData(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            user             = request.user
            permission_model = user.permissions_set.first()
            permission       = permission_model.can_edit_users_data
            return permission
        except AttributeError:
            return False
        
        
        
class CanEditExamResults(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            user             = request.user
            permission_model = user.permissions_set.first()
            permission       = permission_model.can_edit_exam_results
            return permission
        except AttributeError:
            return False
        
        
        
class CanSeeIntakeLevelStatistics(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            user             = request.user
            permission_model = user.permissions_set.first()
            permission       = permission_model.see_intake_level_statistics
            return permission
        except AttributeError:
            return False



     
class CanEditExam(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            user             = request.user
            permission_model = user.permissions_set.first()
            permission       = permission_model.can_edit_exam
            print(permission_model)
            print(permission)
            return permission
        except AttributeError:
            return False
        
        
class CanEditSubject(permissions.BasePermission):
    def has_permission(self, request, view):
        try:
            user             = request.user
            permission_model = user.permissions_set.first()
            permission       = permission_model.can_edit_subject
            print(permission_model)
            print(permission)
            return permission
        except AttributeError:
            return False
        
class CanEditLevel(permissions.BasePermission):     
    def has_permission(self, request, view):
            try:
                user             = request.user
                permission_model = user.permissions_set.first()
                permission       = permission_model.can_edit_level
                print(permission_model)
                print(permission)
                return permission
            except AttributeError:
                return False
        
class IsStudent(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff