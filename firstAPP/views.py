from django.shortcuts import render
from django.http import response, HttpResponse, HttpResponseNotFound


# Create your views here.

# def index(request):
#     return HttpResponse("It Works!!")

def daily_challenges(request, month):
    match month:
        case "january":
            return HttpResponse("Walk for 30 min daily")
        case "february":
            return HttpResponse("Eat no meat")
        case "march":
            return HttpResponse("study django for two hours daily")
        case _:
            return HttpResponseNotFound("Sorry, I don't know what you are looking for")