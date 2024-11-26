from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegisterForm

users = ['KyberSlavik', 'Biber', 'UltraUrban']

def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if password != repeat_password:
                info['error'] = "Пароли не совпадают."
            elif age < 18:
                info['error'] = "Возраст должен быть не менее 18 лет."
            elif username in users:
                info['error'] = "Логин уже занят."
            else:
                return HttpResponse(f"Приветствуем, {username}!")
    else:
        form = UserRegisterForm()
    info['form'] = form
    return render(request, 'registration_page.html', info)



def sign_up_by_html(request):
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))
        if password != repeat_password:
            info['error'] = "Пароли не совпадают."
        elif age < 18:
            info['error'] = "Возраст должен быть не менее 18 лет."
        elif username in users:
            info['error'] = "Логин уже занят."
        else:
            return HttpResponse(f"Приветствуем, {username}!")
    return render(request, 'registration_page.html', info)
