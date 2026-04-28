from django.shortcuts import render
from django.http import response, HttpResponse


# Create your views here.

def index(request):
    return HttpResponse("It Works!!")

