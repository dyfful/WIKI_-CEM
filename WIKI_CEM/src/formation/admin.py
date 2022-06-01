from webbrowser import get

from django.contrib import admin
from formation.models import Doc, Lien, Footer


@admin.register(Doc)
class DocAdmin(admin.ModelAdmin):
    list_display = ("libelle", "nomButton", "url")
    empty_value_display = "Inconnu"
    search_fields = ("libelle", "nomButton")
    # filter_horizontal = ('Groupement', 'ACR', 'Poste')


@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    list_display = ("Titre", )
    empty_value_display = "Inconnu"
    search_fields = ("Titre", )


@admin.register(Lien)
class LienAdmin(admin.ModelAdmin):
    list_display = ("nom", "url")
    empty_value_display = "Inconnu"
    search_fields = ("nom", "url")
    # list_editable = ("url", )
