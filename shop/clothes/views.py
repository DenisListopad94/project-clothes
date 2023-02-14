from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')

def all_clothes(request):
    return render(request, 'all_clothes.html')
