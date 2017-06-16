from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    context = ""
    return render(request, 'todo/index.html', context)

def signup(request):
    context = ""
    return render(request, 'todo/signup.html', context)