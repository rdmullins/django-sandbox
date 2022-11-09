from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('superheroes/', views.superheroes),
    path('abilities/', views.abilities),
]
