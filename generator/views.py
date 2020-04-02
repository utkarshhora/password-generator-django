from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html', {'password': random.randrange(100)})

def password(request):
    numbers = list('1234567890')
    special_Char = list('!@#$%^&*<>?+')
    characters = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length'))
    password = ''

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('Special characters'):
        characters.extend(special_Char)
    if request.GET.get('numbers'):
        characters.extend(numbers)

    for x in range(length):
        password += characters[random.randrange(len(characters)-1)]

    return render(request, 'generator/password.html', {'password': password})

def about(request):
    return render(request, 'generator/about.html')
