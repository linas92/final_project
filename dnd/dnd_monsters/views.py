from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "dnd_monsters/homepage.html")

    # return render(request, 'library/index.html', context) context ?