from django.contrib.auth import get_user_model
from django.db import models
from django.utils.html import format_html
from django.urls import reverse
from tinymce.models import HTMLField


class Size(models.Model):
    size = models.CharField(max_length=255)
    short_description = models.TextField()
    slug = models.SlugField()

    class Meta:
        ordering = ("size", )

    def __str__(self) -> str:
        return f"{self.size}" 

    # def get_absolute_url(self):
    #     return "/%s/" % self.slug

    # def link_filtered_monsters(self):
    #     link = reverse('monsters')+'?size_id='+str(self.id)
    #     return format_html('<a class="size" href="{link}">{monster_size}</a>', link=link, name=self.monster_size)


class Type(models.Model):
    monster_type = models.CharField("monster type", max_length=200, help_text="Enter the type of the beast/monster",)
    slug = models.SlugField()
    # CombatClass foreign key

    def __str__(self) -> str:
        return self.monster_type

    def get_absolute_url(self):
        return "/%s/" % self.slug

    def link(self) -> str:
        link = reverse('type', kwargs={'type_id':self.id})
        return format_html('<a href="{link}">{type}</a>', link=link, type=self.__str__())


class Monster(models.Model):
    ACTIVE = "active"
    DRAFT = "draft"

    CHOICES_STATUS = (
        (ACTIVE, "Active"),
        (DRAFT, "Draft")
    )

    name = models.CharField("name", max_length=50)
    about = models.TextField('summary')
    image = models.ImageField("image", upload_to='images', blank=True, null=True)
    slug = models.SlugField()
    sizes = models.ForeignKey(Size, on_delete=models.SET_NULL, null=True, blank=True, related_name="monsters", )
    types = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True, blank=True, related_name="monsters", )
    # CombatClass foreign key
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=CHOICES_STATUS, default=ACTIVE)


    class Meta:
        ordering = ("-created_at", )

    def __str__(self) -> str:
        return f"{self.name} {self.types} {self.sizes}"

    def get_absolute_url(self):
        return "/%s/%s/" % (self.types.slug, self.slug)

    # def display_size(self) -> str:
    #     return ', '.join(size.name for size in self.size.all()[:3])
    # display_size.short_description = 'size(s)'




#       MAKE ANOTHER FIELD FOR LEVELS, HAVE IT HAVE A FOREIGNKEY-> SIZES AND MONSTERS

# class Level(models.Model):
#     level = models.CharField("")
#     level = models.ForeignKey(Monster, verbose_name="monster", on_delete=models.CASCADE, related_name='append',)
#     geek = models.ForeignKey(get_user_model(), verbose_name="geek", on_delete=models.CASCADE, related_name='lore_append',)

#     created_at = models.DateTimeField("created at", auto_now_add=True)
#     # text_ = models.TextField("content", max_length=10000)

#     def __str__(self):
#         pass

#     class Meta:
#         ordering = ('-created_at', )

#         #MAKE A POSSIBILITY TO COMMENT ON A MONSTER
class Comment(models.Model):
    monster = models.ForeignKey(Monster, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)



# class Abilities(models.Model):
#     pass
# CombatClass foreign key


    # MAKE IT HAVE COMBAT CLASSES - spell caster, fighter, range or w/e FOREIGNKEY monsters, types, 
# class CombatClass(models.Model):
#     pass
# Abilities foreign key