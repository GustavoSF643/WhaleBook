from rest_framework.permissions import BasePermission, SAFE_METHODS
from groups.models import GroupUser

class IsLeaderOfGroupOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        try:
            user_type = GroupUser.objects.get(group_id=int(view.kwargs['pk']), user_id=request.user.id) 
            return user_type.is_admin
        except:
            return False
