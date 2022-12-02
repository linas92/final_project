from django.contrib.auth import get_user_model
from django.db import models
from django.utils.html import format_html
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from tinymce.models import HTMLField



class Monster(models.Model):
    name = models.CharField(_("name"), max_length=50)
    about = HTMLField(_('summary'))
    size = models.ForeignKey(Size, on_delete=models.SET_NULL, null=True, blank=True, related_name="monsters", )
    type = models.ManyToManyField(Type, help_text=_('Choose type(s) for this monster'), verbose_name=_('type(s)'), )
    image = models.ImageField(_("image"), upload_to='images', blank=True, null=True)

    def __str__(self) -> str:
        return f"The monster is called {self.name}, size varies {self.size}, they are {self.type} type"

    def display_size(self) -> str:
        return ', '.join(size.name for size in self.size.all()[:3])
    display_size.short_description = _('size(s)')


class Type(models.Model):
    monster_type = models.CharField(_("monster type"), max_length=200, help_text=_("Enter the type of the beast/monster"),)

    def __str__(self) -> str:
        return self.monster_type

    def display_monsters(self) -> str:
        return ', '.join(monster.name for monster in self.monsters.all())
    display_monsters.short_description = _('monsters')

    def link(self) -> str:
        link = reverse('type', kwargs={'type_id':self.id})
        return format_html('<a href="{link}">{type}</a>', link=link, type=self.__str__())

    class Meta:
        ordering = ["monster_tpe", ]
        verbose_name = _("type")
        verbose_name_plural = _("types")


class Size(models.Model):
    monster_size = models.CharField(_("monster size"), max_length=50, help_text=_("Enter the monsters size"), )
    # tiny = models.CharField(_("tiny"), help_text=_("from 0cm. (just saying, it's DnD, whatever you imagine) up to 75cm. (0ft. - 2,5ft.)"), )
    # small = models.CharField(_("tiny"), help_text=_("from 75cm. up to 1,5m. (2,5ft. - 5ft."), )
    # medium = models.CharField(_("medium"), help_text=_("from 1,5m. up to 3m. (5ft. - 10ft.)"), )
    # large = models.CharField(_("large"), help_text=_("from 3m. up to 4,5m. (10ft. - 15ft.)"), )
    # huge = models.CharField(_("huge"), help_text=_("from 4,5m. up to 6m. (15ft. - 20ft.)"), )
    # gargantuan = models.CharField(_("gargantuan"), help_text=_("from 6m. up to whatever (20ft. - up to whatever)"), )

    # def __str__(self) -> str:
    #     return f"Size of the creature: {self.tiny}, {self.small}, {self.medium}, {self.large}, {self.huge}, {self.gargantuan}"

    def __str__(self) -> str:
        return self.monster_size

    def link_filtered_monsters(self):
        link = reverse('monsters')+'?size_id='+str(self.id)
        return format_html('<a class="size" href="{link}">{monster_size}</a>', link=link, name=self.monster_size)




class Lore(models.Model):
    monster = models.ForeignKey(Monster, verbose_name=_("monster"), on_delete=models.CASCADE, related_name='append',)
    geek = models.ForeignKey(get_user_model(), verbose_name=_("geek"), on_delete=models.CASCADE, related_name='lore_append',)




    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    text_ = models.TextField(_("content"), max_length=10000)

    #reikia pasidaryti __str__(self):

    
    # class Meta:
    #     ordering = ('-created_at', )
    # gal ir reikes
        
         