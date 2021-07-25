from django.db import models


# Create your models here.

class Origin(models.Model):
    name = models.CharField(max_length=60, unique=True, verbose_name="网站名")
    domain = models.CharField(max_length=70, unique=True, verbose_name="域名")
    rule = models.JSONField(verbose_name="匹配规则")

    # def _validate(self):
    #     for key in ["chapter", ""]
    #     raise ValueError("rule error")
    #
    # def save(self, force_insert=False, force_update=False, using=None,
    #          update_fields=None):
    #     print("in save ")
    #     super().save(force_insert, force_update, using, update_fields)


class Author(models.Model):
    name = models.CharField(max_length=100, blank=False, verbose_name="作者名")
    introduction = models.TextField(default="暂无简介", verbose_name="简介")


class Novel(models.Model):
    name = models.CharField(max_length=200, blank=False, verbose_name="小说名")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="作者")
    uid = models.CharField(max_length=100, unique=True, verbose_name="UID",
                           help_text="md5(novelName_id;novelAuthor_id)")
