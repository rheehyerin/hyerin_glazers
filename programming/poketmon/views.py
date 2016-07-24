from django.shortcuts import render
from .models import User, Pokemon, Capture

# Create your views here.
def pokemon(request):
    capture_list = Capture.objects.all()
    return render(request, 'poketmon/pokemon.html', {'capture_list':capture_list}) #전자의 user_list의 이름은 html에서 쓰여질 이름. 후자의 user_list는 querySet
