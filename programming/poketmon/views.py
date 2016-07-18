from django.shortcuts import render
from .models import User, Pokemon, Place

# Create your views here.
def pokemon(request):
    user_list = User.objects.all()
    return render(request, 'poketmon/pokemon.html', {'user_list':user_list})


