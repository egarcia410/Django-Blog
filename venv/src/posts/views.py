from django.http import HttpResponse
from django.shortcuts import render

def posts_home(request):
    return HttpResponse('<h1>Hello</h1>')


# Create your views here.
