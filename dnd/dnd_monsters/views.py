from django.shortcuts import render


def homepage(request):
    return render(request, "dnd_monsters/homepage.html")

def monsterspage(request):
    return render(request, "dnd_monsters/monsterspage.html")

def npcpage(request):
    return render(request, "dnd_monsters/npcpage.html")

def playerspage(request):
    return render(request, "dnd_monsters/playerspage.html")

    # return render(request, 'library/index.html', context) context ?