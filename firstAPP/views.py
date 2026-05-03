from django.shortcuts import render
from django.http import response, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


monthly_challenges = {
    "january": "Eat no meat for the entire month",
    "february": "study django for 2 hours daily",
    "march": "walk for 20 minutes daily",
    "april": "study for aws data engineer certificate",
    "may": "study for apache spark and big data",
    "june": "study python to the advanced level",
    "july": "study sql to the advanced level",
    "august": "do some data engineering projects",
    "september": "learn data warehousing using snowflake",
    "october": "do some data warehousing projects",
    "november": "learn and do projects about kafka",
    "december": "do some excercises every morning"

}


# Create your views here.
def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)




def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    redircted_month = months[month - 1]
    return HttpResponseRedirect("/challenges/" + redircted_month)


def daily_challenges(request, month):
    try:
        return HttpResponse(monthly_challenges[month])
    except:
        return HttpResponseNotFound("this month is not found")
