import os
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, reverse
from os import listdir

def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir'),
    }

    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = datetime.today()
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    template_name2 = 'app/workdir.html'
    dir = os.listdir()

    return HttpResponse(dir)
