from common.views import ReturnMsg
from rest_framework.response import Response
from Blog.settings import JWT_AUTH


def jwt_response_payload_handler(token, user=None, request=None):
    """为返回的结果添加相关信息"""

    token_data = {
        "token": token,
        "expire_times": JWT_AUTH['JWT_EXPIRATION_DELTA'].total_seconds()
    }

    return ReturnMsg(data=token_data).dict()
