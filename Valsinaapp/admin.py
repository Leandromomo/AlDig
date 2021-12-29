from django.contrib import admin

from .models import Publicidad


class PublicidadAdmin(admin.ModelAdmin):

    readonly_fields=("created","updated")

admin.site.register(Publicidad, PublicidadAdmin)



# Register your models here.
