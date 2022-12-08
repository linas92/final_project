from django.contrib import admin
from . import models


class MonsterAdmin(admin.ModelAdmin):
    search_fields = ["name", "sizes", "types", ]
    list_display = ["types", "sizes", "created_at", ]
    list_filter = ["types", "sizes", "created_at", ]


class TypeAdmin(admin.ModelAdmin):
    search_fields = ["types", ]


admin.site.register(models.Size)
admin.site.register(models.Monster, MonsterAdmin)
admin.site.register(models.Type, TypeAdmin)
# admin.site.register(models.Lore)