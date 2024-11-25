from django.shortcuts import render, redirect
from .models import Image



def main(request):
    title = 'Tripleware'
    h1_p = 'Главная страница'
    first = 'Главная'
    second = 'Продукты разработчика'
    third = 'Корзина'
    context = {
        'title': title,
        'h1_p': h1_p,
        'first': first,
        'second': second,
        'third': third,
    }
    return render(request, 'main_page.html', context)


def second_page(requests):
    title = 'Products'
    h1_p = 'Продукты разработчика'
    first = 'Killing floor'
    second = 'Killing floor 2'
    third = 'Killing floor: Incursion'
    fourth = 'Killing floor 3'
    main_p = 'На главную'
    context = {
        'title': title,
        'h1_p': h1_p,
        'first': first,
        'second': second,
        'third': third,
        'fourth': fourth,
        'main_p': main_p,
    }
    return render(requests, 'second_page.html', context)


def third_page(requests):
    title = 'Basket'
    h1_p = 'Ваши покупки:'
    main_p = 'На главную'
    if_none = 'Кажется здесь пусто :)'
    context = {
        'h1_p': h1_p,
        'main_p': main_p,
        'if_none': if_none,
        'title': title,
    }
    return render(requests, 'third_page.html', context)
