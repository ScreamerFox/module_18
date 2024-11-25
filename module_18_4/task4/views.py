from django.shortcuts import render, redirect
from .models import Image



def main(request):
    page_name = 'Главная страница'
    menu = ['Главная', 'Продукты разработчика', 'Корзина']
    context = {
        'page_name': page_name,
        'menu': menu,
    }
    return render(request, 'menu.html', context)


def second_page(requests):
    page_name = 'Продукты разработчика'
    menu = ['Главная', 'Продукты разработчика', 'Корзина']
    content = ['Killing floor ', 'Killing floor 2 ', 'Killing floor: Incursion ', 'Killing floor 3 ']
    context = {
        'page_name': page_name,
        'menu': menu,
        'content': content,
    }
    return render(requests, 'second_page.html', context)


def third_page(requests):
    page_name = 'Корзина'
    basket = []
    len_bas = len(basket)
    menu = ['Главная', 'Продукты разработчика', 'Корзина']
    content = 'Кажется здесь пусто :)'
    context = {
        'page_name': page_name,
        'menu': menu,
        'basket': basket,
        'content': content,
        'len_bas': len_bas,
    }
    return render(requests, 'third_page.html', context)
