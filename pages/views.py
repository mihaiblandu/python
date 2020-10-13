from django.shortcuts import render
from django.http import HttpResponse

def social_view(request, *args, **kwargs):
    print(request)
    return HttpResponse("<h1>Home Page</h1>")