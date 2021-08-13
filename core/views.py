from rest_framework import viewsets
from rest_framework import permissions
from core.serializers import ProfileSerializer
from core.models import Profile

class PermissionBasic(viewsets.ModelViewSet):
    "只有 list  和 retrieve 不需要权限"


    # 自定义permission_classes_by_action变量,重写get_permissions来给不同的动作设置不同的权限
    # permission_classes_by_action = {'default': [permissions.IsAuthenticated],
    #                                 'update': [permissions.IsAuthenticated],
    #                                 'destroy': [permissions.IsAuthenticated],
    #                                 'create': [permissions.IsAuthenticated],
    #                                 'list': [],
    #                                 }
    # 重写get_permissions

    def get_permissions(self):
        # if self.action not in  ['list','retrieve']:
        #     return [permissions.IsAuthenticated()]
        return []
        

        # try:
        #     # return permission_classes depending on `action`
        #     return [permission() for permission in self.permission_classes_by_action[self.action]]
        # except KeyError:
        #     # 没用明确权限的话使用默认权限
        #     # action is not set return default permission_classes
        #     return [permission() for permission in self.permission_classes_by_action['default']]


class ProfileViewSet(PermissionBasic):
    """
    
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
