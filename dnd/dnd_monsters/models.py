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
        return f"{self.size_name}" 

    def link_filtered_monsters(self):
        link = reverse('monsters')+'?size_id='+str(self.id)
        return format_html('<a class="size" href="{link}">{monster_size}</a>', link=link, name=self.monster_size)


class Type(models.Model):
    monster_type = models.CharField(_("monster type"), max_length=200, help_text=_("Enter the type of the beast/monster"),)
    # CombatClass foreign key

    def __str__(self) -> str:
        return self.monster_type

    def link(self) -> str:
        link = reverse('type', kwargs={'type_id':self.id})
        return format_html('<a href="{link}">{type}</a>', link=link, type=self.__str__())


class Monster(models.Model):
    name = models.CharField(_("name"), max_length=50)
    about = HTMLField(_('summary'))
    image = models.ImageField(_("image"), upload_to='images', blank=True, null=True)
    sizes = models.ForeignKey(Size, on_delete=models.SET_NULL, null=True, blank=True, related_name="monsters", )
    types = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True, blank=True, related_name="monsters", )
    # CombatClass foreign key
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_at", )

    def __str__(self) -> str:
        return f"{self.name} {self.types} {self.sizes}"

    def display_size(self) -> str:
        return ', '.join(size.name for size in self.size.all()[:3])
    display_size.short_description = _('size(s)')



    ################## DO NOT DELETE, COPY-PASTA INTO ADMIN SIZES CATEGORY

    # Gargantuan From 6m. up to whatever size (20ft. - up to whatever)
    # Huge From 4,5m. up to 6m. (15ft. - 20ft.)
    # Large From 3m. up to 4,5m. (10ft. - 15ft.)
    # Medium From 1,5m. up to 3m. (5ft. - 10ft.)
    # Small From 75cm. up to 1,5m. (2,5ft. - 5ft.)
    # Tiny From 0cm. up to 75cm. (0ft. - 2,5ft.) It's DnD, whatever floats your boat, imagination is infinite


#       MAKE ANOTHER FIELD FOR LEVELS, HAVE IT HAVE A FOREIGNKEY-> SIZES AND MONSTERS
# class Level(models.Model):
#     level = models.CharField("")
#     level = models.ForeignKey(Monster, verbose_name=_("monster"), on_delete=models.CASCADE, related_name='append',)
#     geek = models.ForeignKey(get_user_model(), verbose_name=_("geek"), on_delete=models.CASCADE, related_name='lore_append',)

#     created_at = models.DateTimeField(_("created at"), auto_now_add=True)
#     # text_ = models.TextField(_("content"), max_length=10000)

#     def __str__(self):
#         pass

#     class Meta:
#         ordering = ('-created_at', )

#         #MAKE A POSSIBILITY TO COMMENT ON A MONSTER
# class Comment(models.Model):
#     pass

        # 
# class Abilities(models.Model):
#     pass
# CombatClass foreign key


    # MAKE IT HAVE COMBAT CLASSES - spell caster, fighter, range or w/e FOREIGNKEY monsters, types, 
# class CombatClass(models.Model):
#     pass
# Abilities foreign key