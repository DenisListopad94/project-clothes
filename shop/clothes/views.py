from django.shortcuts import render
from django.http import HttpResponse

clothes = [
    {"name": "jeans", "costs": 70},
    {"name": "short", "costs": 47},
    {"name": "sweter", "costs": 280},
    {"name": "coat", "costs": 370},
    {"name": "t-short", "costs": 40},
    {"name": "belt", "costs": 28},
    {"name": "trouses", "costs": 150},
    {"name": "suit", "costs": 500},
    {"name": "snickers", "costs": 250},
]


def index(request):
    return render(request, 'index.html', )


def all_clothes(request):
    return render(request, 'all_clothes.html', {'clothes': clothes})
