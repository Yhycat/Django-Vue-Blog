from django.db import models

# Create your models here.


class Profile(models.Model):
    '''profile 信息'''

    avater = models.ImageField(
        "头像", upload_to="images/", height_field=None, width_field=None, max_length=None)
    descriotion = models.CharField("描述", max_length=254)
    email = models.EmailField("联系邮箱", max_length=254)
    github = models.URLField("github地址", max_length=200)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profile"

    # def __str__(self):
    #     return self.name

    # def get_absolute_url(self):
    #     return reverse("Profile_detail", kwargs={"pk": self.pk})


class Tag(models.Model):
    '''文章 标签'''

    name = models.CharField("名字", max_length=50)

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"


class Category(models.Model):
    '''文章 分类'''

    name = models.CharField("名字", max_length=50)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categorys"


      