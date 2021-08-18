import datetime

from rest_framework import viewsets, permissions, status
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSetMixin
from rest_framework.response import Response

from rest_framework.decorators import action
# 公共 viewset 
from common.views import CustomViewSet

# 过滤
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
# 分页配置
from Blog.config import StandardResultsSetPagination

# model 和 serializers
from core.serializers import ProfileSerializer, TagSerializer, CategorySerializer, ArticleSerializer
from core.models import Profile, Tag, Category, Article

# response消息
from common.views import ReturnMsg


class UserViewSet(ViewSetMixin, APIView):
    """
    用户认证
    """

    def auth(self,request):
        data = {
            "is_superuser":request.user.is_superuser
        }
        return Response(ReturnMsg(data=data).dict(), status=status.HTTP_200_OK)


class ProfileViewSet(CustomViewSet):
    """
    简介信息
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    # def update(self, request, pk=None, *args, **kwargs):
    #     pass

class TagViewSet(CustomViewSet):
    """
    标签
    """
    queryset = Tag.objects.filter(is_delete=0)
    serializer_class = TagSerializer
    search_fields = ('name',)



class CategoryViewSet(CustomViewSet):
    """
    分类
    """
    queryset = Category.objects.filter(is_delete=0)
    serializer_class = CategorySerializer
    search_fields = ('name',)


class ArticleViewSet(CustomViewSet):
    """
    文章
    """
    queryset = Article.objects.filter(is_delete=0)
    serializer_class = ArticleSerializer
    # 分页
    pagination_class = StandardResultsSetPagination
    # 过滤
    # filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    # filter_class = GoodsFilters
    filter_fields = ('tag', 'category')

    # 搜索
    # search_fields = ('title','content_md')
    # 排序
    # ordering_fields = ('sold_num', 'shop_price')

    # 自定义方法

    @action(methods=['post'], detail=False, url_path='search')
    def search(self, request, *args, **kwargs):
        dd = {"w": "ww", "ee": "ttt"}
        return Response(dd)

    # def list(self, request):
    #     pass

    def create(self, request):

        # 获取 category 和 tag
        category_data = request.data.get(
            "category") if request.data.get("category") else []
        tag_data = request.data.get('tag') if request.data.get("tag") else []

        category = [
            Category.get_or_create(i) for i in category_data if i
        ]
        tag = [Tag.get_or_create(i) for i in tag_data if i]

        # 构造 create 需要的数据
        data = dict()
        data['title'] = request.data.get('title')
        data['content_md'] = request.data.get('content_md')
        data['content_html'] = request.data.get('content_html')
        data['tag'] = tag
        data['category'] = category
        # data['update_time'] = datetime.datetime.now()

        serializer = ArticleSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)

        return Response({
            'code': 20000,
            'message': '文章发布成功'
        },
            status=status.HTTP_200_OK)
    # def retrieve(self, request, pk=None):
    #     pass

    # def update(self, request, pk=None):
    #     pass

    # def partial_update(self, request, pk=None):
    #     pass

    def destroy(self, request, pk=None):
        # 逻辑删除
        Article.objects.filter(pk=pk).update(is_delete=1)
        article = Article.objects.get(pk=pk)

        # 减少分类 标签 引用次数
        for i in article.tag.values():
            tag = Tag.objects.get(id=i['id'])
            # 减少引用次数
            tag.decrease_citations()

        for ii in article.category.values():
            category = Category.objects.get(id=i['id'])
            # 减少引用次数
            category.decrease_citations()

        return Response({'code': 20000, 'message': "删除成功"})
