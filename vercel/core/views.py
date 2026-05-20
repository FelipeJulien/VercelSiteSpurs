from django.shortcuts import render
from .models import Player, Championship, HistoryEvent


def home(request):
    championships = Championship.objects.all()
    return render(request, 'core/home.html', {'championships': championships})


def roster(request):
    players = Player.objects.filter(is_active=True, is_legend=False)
    return render(request, 'core/roster.html', {'players': players})


def history(request):
    events = HistoryEvent.objects.all()
    legends = Player.objects.filter(is_legend=True)
    championships = Championship.objects.all()
    return render(request, 'core/history.html', {
        'events': events,
        'legends': legends,
        'championships': championships,
    })


def arena(request):
    return render(request, 'core/arena.html')
