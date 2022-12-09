from django.contrib import admin
from . import models


class CommentItemInLine(admin.TabularInline):
    model = models.Comment
    raw_id_fields = ["monster"]


class MonsterAdmin(admin.ModelAdmin):
    search_fields = ["name", "sizes", "types", ]
    list_display = ["types", "sizes", "slug", "created_at", "status", ]
    list_filter = ["types", "sizes", "created_at", "status", ]
    prepopulated_fields = {"slug": ("name",)}
    inlines = [CommentItemInLine]
    prepopulated_fields = {"slug": ("name",)}


class TypeAdmin(admin.ModelAdmin):
    search_fields = ["monster_type", ]
    prepopulated_fields = {"slug": ("monster_type",)}


class CommentAdmin(admin.ModelAdmin):
    list_display = ["name", "monster", "created_at", ]


class SizeAdmin(admin.ModelAdmin):
    search_fields = ["size", ]
    prepopulated_fields = {"slug": ("size",)}



admin.site.register(models.Comment, CommentAdmin, )
admin.site.register(models.Size, SizeAdmin)
admin.site.register(models.Monster, MonsterAdmin, )
admin.site.register(models.Type, TypeAdmin, )
# admin.site.register(models.Lore)