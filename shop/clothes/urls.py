from django.urls import path
from .views import index, all_clothes

urlpatterns = [
    path('index/', index, name='home'),
    path('all_clothes/', all_clothes, name='all_clothes'),
]