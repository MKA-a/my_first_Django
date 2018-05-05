from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=32, unique=True, verbose_name='Название')
    desc = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=32, unique=True, verbose_name='Название')
    price = models.PositiveIntegerField(verbose_name='Цена')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ProductImg(models.Model):
    img = models.ImageField(upload_to='products', null=True, default='/')
    name_product = models.ForeignKey(Product, on_delete=models.CASCADE)


class MarketingNew(models.Model):
    name = models.ForeignKey(Product, on_delete=models.CASCADE)
    desc = models.TextField(blank=True)
    img = models.ForeignKey(ProductImg, on_delete=models.CASCADE)


class MarketingPopular(models.Model):
    name = models.ForeignKey(Product, on_delete=models.CASCADE)
    desc = models.TextField(blank=True)
    img = models.ForeignKey(ProductImg, on_delete=models.CASCADE)


class MarketingSale(models.Model):
    name = models.ForeignKey(Product, on_delete=models.CASCADE)
    desc = models.TextField(blank=True)
    img = models.ForeignKey(ProductImg, on_delete=models.CASCADE)
