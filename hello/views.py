from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def Home(request):
    return HttpResponse("Hello, home!")

def FrontP(request):
    return HttpResponse("Welcome to the front page")

def greet(request, name):
    return render(request, "hello/greet.html",{
        "name": name
    })