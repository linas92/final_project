from django.db import models
from django.utils.translation import gettext_lazy as _
from datetime import date



class Monster(models.Model):#kaip book
    name = models.CharField(_("name"), max_length=50)
    size = models.ForeignKey(Size, on_delete=models.SET_NULL, null=True, blank=True, related_name="monsters", )


class Type(models.Model):#kaip genre
    type = models.CharField(_("type"), max_length=200, help_text=_("Enter the type of the beast/monster"))

    def __str__(self) -> str:
        return self.type


class Size(models.Model):#darau kaip authors
    tiny = models.CharField(_())
    small = 
    medium = 
    large = 
    huge = 
    gargantuan = 