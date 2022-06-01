from django.contrib import admin

from theme.models import Fiche, TypeFiche, Commentaire


@admin.register(Fiche)
class FicheAdmin(admin.ModelAdmin):
    list_display = ("TypeFiche", "Titre")
    empty_value_display = "Inconnu"
    search_fields = ("TypeFiche", "Titre", "Contenu")


# @admin.register(TypeFiche)
# class TypeFicheAdmin(admin.ModelAdmin):
#     list_display = ("libelle",)
#     empty_value_display = "Inconnu"
#     search_fields = ("libelle",)


@admin.register(Commentaire)
class CommentaireAdmin(admin.ModelAdmin):
    list_display = ("Nom", "DateCreation", "Titre", "Fiche")
    empty_value_display = "Inconnu"
    search_fields = ("Nom", "DateCreation", "Titre", "Contenu", "Fiche__libelle")
    list_filter = ("DateCreation", "Fiche", "Titre", "Nom")
    readonly_fields = ('Fiche',)