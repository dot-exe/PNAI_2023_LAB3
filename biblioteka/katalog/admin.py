from django.contrib import admin

# Register your models here.

from .models import Autor, Gatunek, Ksiazka, InstacjaKsiazki, Bibliotekarz, Wydawca

# admin.site.register(Autor)
admin.site.register(Gatunek)
# admin.site.register(Ksiazka)
# admin.site.register(InstacjaKsiazki)
admin.site.register(Bibliotekarz)
admin.site.register(Wydawca)


class AutorAdmin(admin.ModelAdmin):
    list_display = ('nazwisko', 'imie', 'data_urodzenia', 'data_smierci')


admin.site.register(Autor, AutorAdmin)


@admin.register(Ksiazka)
class KsiazkaAdmin(admin.ModelAdmin):
    list_display = ('tytul', 'autor', 'display_gatunek')


@admin.register(InstacjaKsiazki)
class InstancjaKsiazkiAdmin(admin.ModelAdmin):
    list_filter = ('status', 'data_zwrotu')
