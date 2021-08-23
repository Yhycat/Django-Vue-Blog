from rest_framework import serializers

from core.models import Profile, Tag, Category, Article


class ProfileSerializer(serializers.HyperlinkedModelSerializer):

    article_num = serializers.SerializerMethodField()
    category_num = serializers.SerializerMethodField()
    tag_num = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ['url', 'avater', 'descriotion', 'email',
                  'github', 'article_num', 'category_num', 'tag_num']

    def get_article_num(self, obj):
        return Article.get_number()

    def get_category_num(self, obj):
        return Category.get_number()


    def get_tag_num(self, obj):
        return Tag.get_number()



class CategorySerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S",
                                            read_only=True)
    update_time = serializers.DateTimeField(
        format="%Y-%m-%d %H:%M:%S",
        read_only=True

    )
    citations = serializers.IntegerField(read_only=True)

    class Meta:
        model = Category
        fields = ['url', 'name', 'citations', 'create_time', 'update_time']


class TagSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S",
                                            read_only=True)
    update_time = serializers.DateTimeField(
        format="%Y-%m-%d %H:%M:%S",
        read_only=True

    )
    citations = serializers.IntegerField(read_only=True)

    class Meta:
        model = Tag
        fields = ['url', 'name', 'citations', 'create_time', 'update_time']


class ArticleSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S",
                                            read_only=True)
    update_time = serializers.DateTimeField(
        format="%Y-%m-%d %H:%M:%S",
        read_only=True
    )
    category = CategorySerializer(
        many=True, required=False)
    tag = TagSerializer(many=True, required=False)

    views = serializers.IntegerField(read_only=True)

    class Meta:
        model = Article
        fields = ['url', 'title', 'category', 'tag', 'views',
                  'content_md', 'content_html', 'create_time', 'update_time']

    def create(self, validated_data):
        category_data = validated_data.pop('category')
        tag_data = validated_data.pop('tag')

        article = Article.objects.create(**validated_data)

        for i in category_data:
            article.category.add(Category.objects.get(name=i['name']))
            # 增加引用次数
            Category.objects.get(name=i['name']).increase_citations()

        for i in tag_data:
            article.tag.add(Tag.objects.get(name=i['name']))
            # 增加引用次数
            Tag.objects.get(name=i['name']).increase_citations()

        return article

    def update(self, instance, validated_data):
        cats_data = validated_data.pop('category')
        tags_data = validated_data.pop('tag')
        instance = super(ArticleSerializer,
                         self).update(instance, validated_data)

        instance.title = validated_data.get('title', instance.title)
        instance.content_md = validated_data.get('content_md',
                                                 instance.content_md)
        instance.content_html = validated_data.get('content_html',
                                                   instance.content_html)
        instance.save()

        for t in instance.tag.values():
            tag = Tag.objects.get(id=t['id'])
            # 减少引用次数
            tag.decrease_citations()

        for t in instance.category.values():
            category = Category.objects.get(id=t['id'])
            # 减少引用次数
            category.decrease_citations()

        instance.tag.clear()
        instance.category.clear()

        for tag_data in tags_data:
            tag_qs = Tag.objects.filter(name__iexact=tag_data['name'])

            tag = tag_qs.first()
            tag.increase_citations()
            instance.tag.add(tag)

        for cat_data in cats_data:
            cat_qs = Category.objects.filter(name__iexact=cat_data['name'])

            cat = cat_qs.first()
            cat.increase_citations()
            instance.category.add(cat)

        return instance
