from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=32, unique=True, verbose_name='Название Категории')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=32, unique=True, verbose_name='Название продукта')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Название Категории')
    short_desc = models.CharField(max_length=64, blank=True, verbose_name='Краткое описание')
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.PositiveIntegerField(verbose_name='Цена')
    img_1 = models.ImageField(upload_to='products', null=True, default=None, verbose_name='Фотография')
    img_2 = models.ImageField(upload_to='products', null=True, default=None, verbose_name='Фотография только перед')
    img_3 = models.ImageField(upload_to='products', null=True, default=None, verbose_name='Фотография только зад')
    marketing = models.IntegerField(default=0, null=True,
                                    verbose_name='0=Без маркетинга, 1=Новинки, 2=Популярные, 3=Распродажа')

    def __str__(self):
        return '{}-{}'.format(self.name, self.category)

