from django.urls import path
from . import views

urlpatterns = [
    path('herolist/', views.herolist),
    path('abilities/', views.abilities),
]