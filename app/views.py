from django.shortcuts import render

from django.http.response import HttpResponse

# Create your views here.


def hey_you(request, name):
    return HttpResponse(f"Hey, {name}!")


def how_old(request, end_year, birth_year):
    return HttpResponse(end_year - birth_year)


def can_i_take_your_order(request, burgers, fries, drinks):
    return HttpResponse(
        "$" + format((burgers * 4.50) + (fries * 1.50) + (drinks * 1.00), ".2f")
    )
