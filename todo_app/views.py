from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def insert(request):
    return render(request, 'insert.html')
