from django.db import models
from django.core import validators


class Info(models.Model):

    name = models.CharField(
        verbose_name='product name',
        max_length=200,
    )
    # image = models.ImageField(upload_to='info/', default='defo')

    created_at = models.DateTimeField(
        verbose_name='registlation date',
        auto_now_add=True
    )


class Item(models.Model):

    SEX_CHOICES = (
        (1, 'man'),
        (2, 'woman'),
        (3, 'child'),
    )

    name = models.CharField(
        verbose_name='product name',
        max_length=200,
    )
    age = models.IntegerField(
        verbose_name='price',
        validators=[validators.MinValueValidator(1)],
        blank=True,
        null=True,
    )
    sex = models.IntegerField(
        verbose_name='gender',
        choices=SEX_CHOICES,
        default=1
    )
    memo = models.TextField(
        verbose_name='add information',
        max_length=300,
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(
        verbose_name='registlation date',
        auto_now_add=True
    )
    description = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to='documents/', default='defo')
    uploaded_at = models.DateTimeField(auto_now_add=True)


    # 以下は管理サイト上の表示設定
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'item'
        verbose_name_plural = 'item'
