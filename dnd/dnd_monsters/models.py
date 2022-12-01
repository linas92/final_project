from django.db import models
from django.utils.translation import gettext_lazy as _
from datetime import date
from tinymce.models import HTMLField



class Monster(models.Model):
    name = models.CharField(_("name"), max_length=50)
    about = HTMLField(_('summary'))
    size = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True, blank=True, related_name="monsters", )
    genre = models.ManyToManyField(Genre, help_text=_('Choose genre(s) for this book'), verbose_name=_('genre(s)'))


class Type(models.Model):
    type = models.CharField(_("type"), max_length=200, help_text=_("Enter the type of the beast/monster"),)

    def __str__(self) -> str:
        return self.type



class Size(models.Model):
    tiny = models.CharField(_("tiny"), help_text=_("from 0cm. (just saying, it's DnD, whatever you imagine) up to 75cm. (0ft. - 2,5ft.)"), )
    small = models.CharField(_("tiny"), help_text=_("from 75cm. up to 1,5m. (2,5ft. - 5ft."), )
    medium = models.CharField(_("medium"), help_text=_("from 1,5m. up to 3m. (5ft. - 10ft.)"), )
    large = models.CharField(_("large"), help_text=_("from 3m. up to 4,5m. (10ft. - 15ft.)"), )
    huge = models.CharField(_("huge"), help_text=_("from 4,5m. up to 6m. (15ft. - 20ft.)"), )
    gargantuan = models.CharField(_("gargantuan"), help_text=_("from 6m. up to whatever (20ft. - up to whatever)"), )

    def __str__(self) -> str:
        return f"Size of the creature: {self.tiny}, {self.small}, {self.medium}, {self.large}, {self.huge}, {self.gargantuan}"


class Lore(models.Model):
    monster = models.ForeignKey(Monster, verbose_name=_("monster"), on_delete=models.CASCADE, related_name='append',)


