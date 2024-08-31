from django.shortcuts import render
from .models import Player

def home(request):
    players = Player.objects.all()
    return render(request, 'home.html', {'players': players})

def player_detail(request, player_id):
    player = Player.objects.get(id=player_id)
    return render(request, 'player_detail.html', {'player': player})

