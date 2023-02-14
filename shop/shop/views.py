from django.http import HttpResponse


def home(request):
    name = "Denis"
    age = 28
    return HttpResponse(f'<h1>home page my name is {name} age {age}</h1>')

def numbers(request, numb):
    return HttpResponse(f'<h1>numb url is {numb}</h1>')
