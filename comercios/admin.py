from django.contrib import admin

from .models import CategoriaComer, Negocio
# Register your models here.


class CategoriaComerAdmin(admin.ModelAdmin):

    readonly_fields=("created","updated")

class ComercioAdmin(admin.ModelAdmin):

    readonly_fields=("created","updated")

admin.site.register(CategoriaComer, CategoriaComerAdmin)

admin.site.register(Negocio, ComercioAdmin)
