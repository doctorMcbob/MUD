from django.shortcuts import render
from lobby.models import Game


def homeview(request):
    games = Game.objects.filter(is_open=True).all()
    context = {"games": games}
    return render(request, 'home.html', context=context)
