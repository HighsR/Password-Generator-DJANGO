import string

from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import random

# Create your views here.

def home(request):
    return render(request, 'home.html')

def passgen(request):
    char =list(string.ascii_lowercase)
    if request.GET.get('uppercase'):
        char.extend(list(string.ascii_uppercase))
    if request.GET.get('digits'):
        char.extend(list(string.digits))
    if request.GET.get('symbols'):
        char.extend(list(string.punctuation))
    length = int(request.GET.get('length',12))
    password=""
    for x in range(length):
        password+=random.choice(char)

    return render(request, 'password.html',{'password':password})