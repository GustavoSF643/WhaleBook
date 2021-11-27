from rest_framework.permissions import BasePermission
from groups.models import GroupUser

class IsLeaderOfGroup(BasePermission):
    def has_permission(self, request, view):
        try:
            user_type = GroupUser.objects.get(group_id=int(view.kwargs['pk']), user_id=request.user.id)      
            return user_type.is_admin
        except:
            return False