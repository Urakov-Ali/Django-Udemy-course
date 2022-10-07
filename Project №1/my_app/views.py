from curses.ascii import HT
from urllib import request
from django.shortcuts import render
import random


def home_View(request):
    return render(request, 'home.html')

def pass_View(request):
    letters = list('qwertyuioplkjhgfdsazxcvbnm')
    if request.GET.get('uppercase'):
        letters.extend(list('QWERTYUIOPLKJHGFDSAZXCVBNM'))
    if request.GET.get('numbers'):
        letters.extend(list('0123456789'))
    if request.GET.get('characters'):
        letters.extend(list('!@#$%^&*()-=+_?:"'))

    length = int(request.GET.get('lenght'))
    password = ''
    for x in range(length):
        password += random.choice(letters)
    return render(request, 'password.html', {'password':password})

def about_View(request):
    ctx = {
        'name':'Mukhammad_Ali',
        'func':'Creating a random password'
    }
    return render(request, 'about.html', ctx)


