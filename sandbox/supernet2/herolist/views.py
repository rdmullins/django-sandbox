from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Superhero, Abilities


# Create your views here.
def herolist(request):
    heroes = list(Superhero.objects.values())
    return JsonResponse({ 'data': heroes})
    # return HttpResponse(heroes)
    # return HttpResponse("This is going to be a list of heroes from the DB.")

def abilities(request):
    abilities = list(Abilities.objects.values())
    return JsonResponse({ 'data': abilities})
    # return HttpResponse("<h1>This</h1><h2>Is going to be</h2><h3>a listing</h3><h4>Of superpowers!</h4>")

# def get_users(request):
#     users = User.objects.all().values('first_name', 'last_name')  # or simply .values() to get all fields
#     users_list = list(users)  # important: convert the QuerySet to a list object
#     return JsonResponse(users_list, safe=False)