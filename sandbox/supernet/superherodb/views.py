from django.shortcuts import render

# Create your views here.
def superheroes(request):
    return HttpResponse("This is where you would see all the superheroes.")

def abilities(request):
    return HttpResponse("This is where you would see all the abilities.")