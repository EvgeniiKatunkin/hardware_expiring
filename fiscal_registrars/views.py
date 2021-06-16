from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """Главная страница с выбором типа оборудования для вывода в виде таблицы."""
    return HttpResponse("That's the only page")
