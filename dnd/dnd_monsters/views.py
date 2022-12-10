from django.shortcuts import render
from gamemaster.models import Monster


def homepage(request):
    return render(request, "dnd_monsters/homepage.html")

def monsterspage(request):
    monsters = Monster.objects.filter(status=Monster.ACTIVE)
    return render(request, "dnd_monsters/monsterspage.html", {"monsters": monsters})

def type(request):
    return render(request, "dnd_monsters/type.html")

def playerspage(request):
    return render(request, "dnd_monsters/playerspage.html")

def npcpage(request):
    return render(request, "dnd_monsters/npcpage.html")