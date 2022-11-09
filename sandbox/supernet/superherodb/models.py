from django.db import models

# Create your models here.

class Relationship(models.Model):
    name = models.CharField(max_length=50) 

class Abilities(models.Model):
    name = models.CharField(max_length=50)

class Superhero(models.Model):
    name = models.CharField(max_length=30)
    about = models.CharField(max_length=100)
    bio = models.CharField(max_length=500)
    relationships = models.ManyToManyField(Relationship)
    abilities = models.ManyToManyField(Abilities)