from django.db import models
import datetime

# Create your models here.
IS_DELETE = ((1, '已删除'), (0, '正常'))


def upload_path(instance, filename):
    return 'images/%s/%s/%s' % (datetime.datetime.now().year, datetime.datetime.now().month, filename)


class Profile(models.Model):
    '''profile 信息'''

    avater = models.ImageField(
        "头像", upload_to=upload_path, height_field=None, width_field=None, max_length=None)
    descriotion = models.CharField("描述", max_length=254)
    email = models.EmailField("联系邮箱", max_length=254)
    github = models.URLField("github地址", max_length=200)

    create_time = models.DateTimeField(auto_now_add=True,
                                       verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True,
                                       verbose_name='更新时间')

    class Meta:
        verbose_name = "简介信息"
        verbose_name_plural = verbose_name


class Category(models.Model):
    name = models.CharField(max_length=16,
                            verbose_name='分类名')
    create_time = models.DateTimeField(auto_now_add=True,
                                       verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True,
                                       verbose_name='更新时间')
    citations = models.IntegerField(default=0, verbose_name='引用次数')
    is_delete = models.IntegerField(choices=IS_DELETE,
                                    default=0,
                                    verbose_name='状态')

    class Meta:
        verbose_name = "分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.name)

    @classmethod
    def get_or_create(cls, v):
        try:
            obj = cls.objects.get(name=v)

        except cls.DoesNotExist:
            obj = cls(name=v)
            obj.save()
        return {'id': obj.id, 'name': obj.name}

    def increase_citations(self):
        self.citations += 1
        self.save(update_fields=['citations'])

    def decrease_citations(self):
        self.citations -= 1
        self.save(update_fields=['citations'])


class Tag(models.Model):
    name = models.CharField(max_length=16, verbose_name='标签名')

    create_time = models.DateTimeField(auto_now_add=True,
                                       verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True,
                                       verbose_name='更新时间')
    citations = models.IntegerField(default=0,  verbose_name='引用次数')
    is_delete = models.IntegerField(choices=IS_DELETE,
                                    default=0,
                                    verbose_name='状态')

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.name)

    @classmethod
    def get_or_create(cls, v):
        try:
            obj = cls.objects.get(name=v)

        except cls.DoesNotExist:
            obj = cls(name=v)
            obj.save()
        return {'id': obj.id, 'name': obj.name}

    def increase_citations(self):
        self.citations += 1
        self.save(update_fields=['citations'])

    def decrease_citations(self):
        self.citations -= 1
        self.save(update_fields=['citations'])


class Article(models.Model):

    title = models.CharField(max_length=50, verbose_name='标题')
    content_md = models.TextField(

        verbose_name='内容markdown格式')
    content_html = models.TextField(

        verbose_name='内容html格式')
    category = models.ManyToManyField(Category)
    tag = models.ManyToManyField(Tag)

    views = models.IntegerField(
        default=0,
        verbose_name='阅读数')
    create_time = models.DateTimeField(auto_now_add=True,
                                       verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True,
                                       verbose_name='更新时间')
    is_delete = models.IntegerField(choices=IS_DELETE,
                                    default=0,
                                    verbose_name='状态')

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = verbose_name
        ordering = ["-create_time"]

    # def __str__(self):
    #     return str(self.title)

    def abstract(self):

        # 自动取前5行
        # 如果有图片 就取图片前
        abstract = ''.join(self.content_html.split('\n')[:6])
        if 'img' in abstract:
            for index, i in enumerate(self.content_html.split('\n')):
                if 'img' in i:
                    return ''.join(self.content_html.split('\n')[:index + 1])
        else:
            return abstract

    def year(self):
        return str(self.create_time).split('-')[0]

    def increase_readings(self):
        self.views += 1
        self.save(update_fields=['views'])
