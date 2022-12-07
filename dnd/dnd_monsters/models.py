from django.contrib.auth import get_user_model
from django.db import models
from django.utils.html import format_html
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from tinymce.models import HTMLField


class Size(models.Model):
    size_name = models.CharField(max_length=255)
    short_description = models.TextField()

    class Meta:
        ordering = ("size_name", )
        verbose_name_plural = "Sizes"

    def __str__(self) -> str:
        return f"{self.size_name} {self.short_description}" 

    def link_filtered_monsters(self):
        link = reverse('monsters')+'?size_id='+str(self.id)
        return format_html('<a class="size" href="{link}">{monster_size}</a>', link=link, name=self.monster_size)


class Type(models.Model):
    monster_type = models.CharField(_("monster type"), max_length=200, help_text=_("Enter the type of the beast/monster"),)
    monster_sizes = models.ForeignKey(Size, related_name="sizes", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.monster_type

    def display_monsters(self) -> str:
        return ', '.join(monster.name for monster in self.monsters.all())
    display_monsters.short_description = _('monsters')

    def link(self) -> str:
        link = reverse('type', kwargs={'type_id':self.id})
        return format_html('<a href="{link}">{type}</a>', link=link, type=self.__str__())

    class Meta:
        # ordering = ["monster_tpe", ""]
        verbose_name = _("type")
        verbose_name_plural = _("types")


class Monster(models.Model):
    name = models.CharField(_("name"), max_length=50)
    about = HTMLField(_('summary'))
    image = models.ImageField(_("image"), upload_to='images', blank=True, null=True)
    sizes = models.ForeignKey(Size, on_delete=models.SET_NULL, null=True, blank=True, related_name="monsters", )
    types = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True, blank=True, related_name="monsters", )

    def __str__(self) -> str:
        return f"The monster is called {self.name}, size varies {self.size}, they are {self.type} type"

    def display_size(self) -> str:
        return ', '.join(size.name for size in self.size.all()[:3])
    display_size.short_description = _('size(s)')



    ######### DO NOT DELETE, COPY-PASTA INTO ADMIN SIZES CATEGORY
    # tiny = models.CharField(_("tiny"), help_text=_("from 0cm. (just saying, it's DnD, whatever you imagine) up to 75cm. (0ft. - 2,5ft.)"), )
    # Monsters range from 0cm.  up to 75cm. (0ft. - 2,5ft.) It's DnD, whatever floats your boat, imagination is infinite)
    # small = models.CharField(_("tiny"), help_text=_("from 75cm. up to 1,5m. (2,5ft. - 5ft."), )
    # Commonly from 75cm. up to 1,5m. (2,5ft. - 5ft.)
    # medium = models.CharField(_("medium"), help_text=_("from 1,5m. up to 3m. (5ft. - 10ft.)"), )
    # Most common encountered creatures. They can be from 1,5m. up to 3m. (5ft. - 10ft.)
    # large = models.CharField(_("large"), help_text=_("from 3m. up to 4,5m. (10ft. - 15ft.)"), )
    # These beings can be from 3m. up to 4,5m. (10ft. - 15ft.)
    # huge = models.CharField(_("huge"), help_text=_("from 4,5m. up to 6m. (15ft. - 20ft.)"), )
    # Rare, but possible to encounter a 4,5m. being, or even up to 6m. (15ft. - 20ft.)
    # gargantuan = models.CharField(_("gargantuan"), help_text=_("from 6m. up to whatever (20ft. - up to whatever)"), )

    ######### DO NOT DELETE, COPY-PASTA INTO ADMIN SIZES CATEGORY



# class Lore(models.Model):
#     monster = models.ForeignKey(Monster, verbose_name=_("monster"), on_delete=models.CASCADE, related_name='append',)
#     geek = models.ForeignKey(get_user_model(), verbose_name=_("geek"), on_delete=models.CASCADE, related_name='lore_append',)

#     created_at = models.DateTimeField(_("created at"), auto_now_add=True)
#     # text_ = models.TextField(_("content"), max_length=10000)

#     def __str__(self):
#         pass

#     class Meta:
#         ordering = ('-created_at', )

        
         