from django.shortcuts import render, redirect
from .models import Image



def main(request):
    title = 'Tripleware'
    context = {
        'title': title,
    }
    return render(request, 'main_page.html', context)


def second(requests):
    title = 'Продукты разработчика'
    img = 'images/backg_kf.jpeg'
    context = {
        'title': title,
    }
    return render(requests, 'second_page.html', context)


def third(requests):
    title = 'Корзина'
    context = {
        'title': title,
    }
    return render(requests, 'third_page.html', context)

