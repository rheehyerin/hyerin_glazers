from django.contrib import admin
from poketmon.models import User, Pokemon, Place
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    display_list =('name', 'get_catched_pokemons')

admin.site.register(User, UserAdmin)
admin.site.register(Pokemon)
admin.site.register(Place)
