from webbrowser import get

from django.contrib import admin
from zone.models import Zone, PO, Groupement, Commentaire, ACR, CategorieZone


@admin.register(Zone)
class ZoneAdmin(admin.ModelAdmin):
    list_display = ("libelle",)
    empty_value_display = "Inconnu"
    search_fields = ("libelle",)
    filter_horizontal = ('Groupement', 'ACR', 'Poste')


@admin.register(CategorieZone)
class CategorieZoneAdmin(admin.ModelAdmin):
    list_display = ("libelle",)
    empty_value_display = "Inconnu"
    search_fields = ("libelle",)


@admin.register(PO)
class POAdmin(admin.ModelAdmin):
    list_display = ("libelle",)
    empty_value_display = "Inconnu"
    search_fields = ("libelle",)


@admin.register(Commentaire)
class CommentaireAdmin(admin.ModelAdmin):
    list_display = ("Nom", "DateCreation", "Titre", "Zone", "Statut")
    empty_value_display = "Inconnu"
    search_fields = ("Nom", "DateCreation", "Titre", "Contenu", "Zone__libelle")
    list_filter = ("DateCreation", "Zone", "Titre", "Nom")
