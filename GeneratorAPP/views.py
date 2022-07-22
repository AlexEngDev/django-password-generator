from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request, 'GeneratorAPP/home.html')

def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        characters.extend(list('£$%&/()/&%'))

    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    length = int(request.GET.get('length',12))

    thepassword = ''
    for x in range(length):
            thepassword += random.choice(characters)

    return render(request, 'GeneratorAPP/password.html',{'password':thepassword})

def info(request):
    return render(request, 'GeneratorAPP/info.html')
