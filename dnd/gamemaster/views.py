from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Monster, Type
from .forms import CommentForm



def detail(request, type_slug, slug):
    monster = get_object_or_404(Monster, slug=slug, status=Monster.ACTIVE)

    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = monster
            comment.save()

            return redirect("monster_detail", slug=slug)
    else:
        form = CommentForm()

    return render(request, "gamemaster/detail.html", {"monster": monster, "form": form})

def type(request, slug):
    type = get_object_or_404(Type, slug=slug)
    monsters = type.monsters.filter(status=Monster.ACTIVE)

    return render(request, "gamemaster/type.html", {"type": type, "monsters": monsters}) 

def search(request):
    query = request.GET.get("query", "")

    monsters = Monster.objects.filter(status=Monster.ACTIVE).filter(Q(name__icontains=query) | Q(about__icontains=query))

    return render(request, "gamemaster/search.html", {"monsters": monsters, "query": query})

