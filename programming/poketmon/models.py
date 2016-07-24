from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return 'Trainer#{} - {}'.format(self.id, self.name)


class Pokemon(models.Model):
    name = models.CharField(max_length=50)
    attack = models.IntegerField(max_length=2)
    defense = models.IntegerField(max_length=2)
    ptype = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Capture(models.Model):
    user = models.ForeignKey(User)
    pokemon = models.ForeignKey(Pokemon)
    location = models.CharField(max_length=100)

    def __str__(self):
        return '{}이(가) {}을(를) {}에서 포획'.format(self.user, self.pokemon, self.location)

