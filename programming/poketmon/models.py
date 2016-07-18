from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=20)
    catched_places = models.ManyToManyField('Place')
    catched_pokemons = models.ManyToManyField('Pokemon')

    def __str__(self):
        return self.name

    def get_catched_pokemons(self):
        return "\n".join([u.catched_pokemons.name for u in self.catched_pokemons.all()])


class Pokemon(models.Model):
    name = models.CharField(max_length=50)
    attack = models.IntegerField(max_length=2)
    defense = models.IntegerField(max_length=2)
    ptype = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Place(models.Model):
    place = models.CharField(max_length=10)

    def __str__(self):
        return self.place

