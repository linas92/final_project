from django.shortcuts import render, get_object_or_404, redirect
from . import models
from django.db.models import Q
from .forms import CommentForm


def detail(request, type_slug, slug):
    monster = get_object_or_404(models.Monster, slug=slug, status=models.Monster.ACTIVE)

    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.monster = monster
            comment.save()

            return redirect("monster_detail", slug=slug)
    else:
        form = CommentForm()

    return render(request, "dnd_monsters/detail.html", {"monster": monster, "form":form})

def homepage(request):
    monsters = models.Monster.objects.all()
    return render(request, "dnd_monsters/homepage.html", {"monsters": monsters})

def monsterspage(request):
    monsters = models.Monster.objects.all()
    return render(request, "dnd_monsters/monsterspage.html", {"monsters": monsters})

def npcpage(request):
    return render(request, "dnd_monsters/npcpage.html")

def playerspage(request):
    return render(request, "dnd_monsters/playerspage.html")

def type(request, slug):
    type = get_object_or_404(models.Type , slug=slug)
    monsters = type.monsters.filter(status=models.Monster.ACTIVE)

    return render(request, "dnd_monsters/type.html", {"type": type, "monsters": monsters, }) 


def search(request):
    query = request.GET.get("query", "")

    monsters = models.Monster.objects.filter(status=models.Monster.ACTIVE).filter(Q(title__icontains=query) | Q(intro__icontains=query) | Q(body__icontains=query))

    return render(request, "dnd_monsters/search.html", {"monsters": monsters, "query": query})
