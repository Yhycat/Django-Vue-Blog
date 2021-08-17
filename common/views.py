from rest_framework import viewsets, permissions,exceptions
from rest_framework.response import Response
from django.http import Http404
from django.core.exceptions import PermissionDenied
from django.db import connections



class ReturnMsg(object):
    """
    公共 返回数据 格式
    """

    def __init__(self, code=1, msg='成功', errors=None, data=None):
        self.code = code
        self.msg = msg
        self.errors = errors if errors else ""
        self.data = data if data else []

    def dict(self):
        return {
            'code': self.code,
            'msg': self.msg,
            'errors': self.errors,
            'data': self.data
        }


class CustomViewSet(viewsets.ModelViewSet):
    """
    公共 viewset 方法 

    自定义返回response数据
    公共权限方法
    """

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return Response(ReturnMsg(data=response.data).dict(), status=response.status_code)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response(ReturnMsg(data=response.data).dict(), status=response.status_code)

    def retrieve(self, request, pk=None , *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        return Response(ReturnMsg(data=response.data).dict(), status=response.status_code)

    def update(self, request, pk=None, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return Response(ReturnMsg(data=response.data).dict(), status=response.status_code)

    def partial_update(self, request, pk=None, *args, **kwargs):
        response = super().partial_update(request, *args, **kwargs)
        return Response(ReturnMsg(data=response.data).dict(), status=response.status_code)

    def destroy(self, request, pk=None, *args, **kwargs):
        response = super().destroy(request, *args, **kwargs)
        return Response(ReturnMsg(data=response.data).dict(), status=response.status_code)

    def get_permissions(self):
        "只有 list  和 retrieve 不需要权限"


        # 搜索不要权限
        if self.name == 'Search':
            return []

        # if self.action not in ['list', 'retrieve']:
        #     return [permissions.IsAdminUser()]
        return []




def set_rollback():
    for db in connections.all():
        if db.settings_dict['ATOMIC_REQUESTS'] and db.in_atomic_block:
            db.set_rollback(True)

def exception_handler(exc, context):
    """
    Returns the response that should be used for any given exception.

    By default we handle the REST framework `APIException`, and also
    Django's built-in `Http404` and `PermissionDenied` exceptions.

    Any unhandled exceptions may return `None`, which will cause a 500 error
    to be raised.

    自定义错误返回 
    """
    if isinstance(exc, Http404):
        exc = exceptions.NotFound()
    elif isinstance(exc, PermissionDenied):
        exc = exceptions.PermissionDenied()

    if isinstance(exc, exceptions.APIException):
        headers = {}
        if getattr(exc, 'auth_header', None):
            headers['WWW-Authenticate'] = exc.auth_header
        if getattr(exc, 'wait', None):
            headers['Retry-After'] = '%d' % exc.wait

        # 源代码
        # if isinstance(exc.detail, (list, dict)):
        #     data = exc.detail
        # else:
        #     data = {'detail': exc.detail}

        # set_rollback()
        # return Response(data, status=exc.status_code, headers=headers)


        # 修改部分
        if isinstance(exc.detail, (list, dict)):
            if isinstance(detail, list):
                errors = exc.detail
            else:
                errors = {k: v[0] for k, v in exc.detail.items()}
        else:
            errors = exc.detail

        set_rollback()
        return Response(
            ReturnMsg(code=0, msg='失败', errors=errors).dict(), status=exc.status_code, headers=headers)

    return None
