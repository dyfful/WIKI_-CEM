from webbrowser import get

from django.contrib import admin

admin.site.site_header = 'Administration du WIKI CEM'  # default: "Django Administration"
# admin.site.index_title = 'Features area'  # default: "Site administration"
admin.site.site_title = 'WIKI CEM'  # default: "Django site admin"

# Register your models here.
from poste.models import Poste, Zone, CategorieZone, PO, Groupement, CategorieConsigne
from poste.models import Client, TypeClient, Consigne, Formation, Theme, Commentaire, ACR


def custom_titled_filter(title):
    class Wrapper(admin.FieldListFilter):
        def __new__(cls, *args, **kwargs):
            instance = admin.FieldListFilter.create(*args, **kwargs)
            instance.title = title
            return instance

    return Wrapper


@admin.register(Poste)
class PosteAdmin(admin.ModelAdmin):
    # list_display = ("idRTE", "libelle", "Impact", "Tension", "statut_sp", "statut_ap", )
    list_display = ("idRTE", "libelle", "Impact", "Tension", "statut_sp", "statut_ap", "getConsigne")

    # @admin.display(description='Consigne associées')
    def getConsigne(self, obj):
         return "\n // ".join([p.libelle for p in obj.Consigne.all()])

    empty_value_display = "Inconnu"
    search_fields = ("idRTE", "libelle", "Impact__libelle", "Tension__libelle", "Consigne__libelle")
    filter_horizontal = ("Consigne",)
    list_filter = (("statut_sp", custom_titled_filter('STATUT SCHÉMA PRÉFÉRENTIEL')), ("statut_ap", custom_titled_filter('STATUT AUTRE PARTICULARITER')), ("Impact__libelle", custom_titled_filter('Impact')), ("Tension__libelle", custom_titled_filter('Tension')), ("Consigne__libelle", custom_titled_filter('Consigne')))


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


@admin.register(Groupement)
class GroupementAdmin(admin.ModelAdmin):
    list_display = ("libelle",)
    empty_value_display = "Inconnu"
    search_fields = ("libelle",)


@admin.register(CategorieConsigne)
class CategorieConsigneAdmin(admin.ModelAdmin):
    list_display = ("libelle",)
    empty_value_display = "Inconnu"
    search_fields = ("libelle",)


@admin.register(Consigne)
class ConsigneAdmin(admin.ModelAdmin):
    list_display = ("libelle",)
    empty_value_display = "Inconnu"
    search_fields = ("libelle",)


@admin.register(TypeClient)
class TypeClientAdmin(admin.ModelAdmin):
    list_display = ("libelle",)
    empty_value_display = "Inconnu"
    search_fields = ("libelle",)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("TypeClient", "libelle", "GMR")
    empty_value_display = "Inconnu"
    search_fields = ("TypeClient__libelle", "libelle", "GMR__libelle")
    filter_horizontal = ('Poste',)
    list_filter = (
        ("TypeClient__libelle", custom_titled_filter('Type Client')), ("GMR__libelle", custom_titled_filter('GMR')),
        ("libelle", custom_titled_filter('Client')),)


@admin.register(Commentaire)
class CommentaireAdmin(admin.ModelAdmin):
    list_display = ("Nom", "DateCreation", "Titre", "Statut", "Poste", "nomImpact")
    # readonly_fields = ["Zone", "Fiche", "Poste"]

    empty_value_display = "Inconnu"

    # @admin.display(description='Impact')
    def nomImpact(self, object):
         return object.Poste.Impact

    search_fields = ("Nom", "DateCreation", "Titre", "Statut__libelle", "Contenu", "Poste__Impact__libelle")
    list_filter = ("DateCreation", ("Poste__Impact__libelle", custom_titled_filter('Impact')),
                   ("Statut__libelle", custom_titled_filter('Statut')),
                   ("Poste__libelle", custom_titled_filter('Poste')), "Titre", "Nom")


@admin.register(Formation)
class FormationAdmin(admin.ModelAdmin):
    list_display = ("Titre",)
    empty_value_display = "Inconnu"
    search_fields = ("Titre",)


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = ("Theme",)
    empty_value_display = "Inconnu"
    search_fields = ("Theme", "ModuleFormation", "QE", "Outils", "Divers")
