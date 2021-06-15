from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """The main page of the fiscal_registrars application."""
    return HttpResponse("That's the only page")
