from django.shortcuts import render
from . import models
from django.db.models import Q



def homepage(request):
    monsters = models.Monster.objects.all()
    return render(request, "dnd_monsters/homepage.html", {"monsters": monsters})

def monsterspage(request):
    return render(request, "dnd_monsters/monsterspage.html")

def npcpage(request):
    return render(request, "dnd_monsters/npcpage.html")

def playerspage(request):
    return render(request, "dnd_monsters/playerspage.html")

def search(request):
    query = request.GET.get("query", "")

    monsters = models.Monster.objects.filter(status=models.Monster.ACTIVE).filter(Q(title__icontains=query) | Q(intro__icontains=query) | Q(body__icontains=query))

    return render(request, "blog/search.html", {"monsters": monsters, "query": query})