from django.shortcuts import render
from datetime import datetime
from django.shortcuts import get_object_or_404
from .models import *


# Create your views here.
def index_view(request):
    products = Product.objects.all()
    now_time = datetime.now()
    marketing_new = MarketingNew.objects.all()
    marketing_popular = MarketingPopular.objects.all()
    marketing_sale = MarketingSale.objects.all()
    product_img = ProductImg.objects.all()

    content = {
        'now_time': now_time,
        'products': products,
        'marketingNew': marketing_new,
        'marketingPopular': marketing_popular,
        'marketingSale': marketing_sale,
        'product_img': product_img
    }
    return render(request, 'mainapp/index.html', content)


def contats_view(request):
    return render(request, 'mainapp/contact.html')


def catalog_apple(request):
    return render(request, 'mainapp/catalog/apple.html')


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