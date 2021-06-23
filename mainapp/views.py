from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import *


# Create your views here.
def index_view(request):
    products = Product.objects.all()
    marketing_new = Product.objects.filter(marketing__startswith=1)
    marketing_popular = Product.objects.filter(marketing__startswith=2)
    # marketing_sale = Product.objects.filter(marketing_startswith=3)

    content = {
        'products': products,
        'marketingNew': marketing_new,
        'marketingPopular': marketing_popular,
        # 'marketingSale': marketing_sale
    }
    return render(request, 'mainapp/index.html', content)


def contats_view(request):
    return render(request, 'mainapp/contact.html')


def catalog_apple(request):
    products_apple = Product.objects.filter(category__pk=1)

    content = {
        'products_apple': products_apple
    }
    return render(request, 'mainapp/catalog/apple.html', content)


def iphone_x(request):
    charectiristic_1 = [{'Тип:': 'смартфон', 'Версия ОС:': 'iOS 11', 'Тип корпуса:': 'классический',
                         'Материал корпуса:': 'стекло', 'Конструкция:': 'водозащита', 'тип SIM:': 'nano SIM',
                         'Количество SIM:': '1', 'Вес:': '174г', 'Размеры (ШхВхТ):': '70,9х143,6х7,7мм',
                         'Тип экрана:': 'цветной OLED, сенсорный'}]

    charectiristic_2 = [{'Тип сенсорного экрана:': 'сультитач, емкостный', 'Диагональ:': '5.8 дюймов',
                         'Сила нажатия на экран:': 'есть', 'Размер изображения:': '2436х1125',
                         'Число пикселей на дюйм:': '463', 'Соотношение сторон:': '19,5:9',
                         'Автоматический поворот экрана:': 'есть', 'Тыловая камера:': 'двойная 12/12 МП',
                         'Фотовспышка:': 'тыльная, светодиодная'}]
    return render(request, 'mainapp/catalog/Apple/iphone_x.html',
                  {'charectiristic_1': charectiristic_1, 'charectiristic_2': charectiristic_2})


# def products(r)