from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """Главная страница с выбором типа оборудования для вывода в виде таблицы."""
    return HttpResponse("Here should be the main page.")
