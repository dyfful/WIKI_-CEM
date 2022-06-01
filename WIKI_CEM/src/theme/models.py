from django.db import models
from poste.models import Statut


class TypeFiche(models.Model):
    libelle = models.CharField(max_length=6)

    def __str__(self):
        return self.libelle


class Fiche(models.Model):
    TypeFiche = models.ForeignKey(TypeFiche, on_delete=models.SET_NULL, null=True)
    Titre = models.CharField(max_length=60)
    image = models.ImageField(upload_to='themes-modop', blank=True)
    Contenu = models.TextField()

    def __str__(self):
        return self.Titre


class CommentaireHistorique(models.Model):
    Nom = models.CharField(verbose_name="Nom", max_length=50, blank=False)
    # Prenom = models.CharField(verbose_name="Prénom", max_length=50, blank=False)
    Date = models.DateTimeField(null=True, blank=True)
    Titre = models.CharField(max_length=80, blank=False)
    Contenu = models.TextField(blank=False)

    # Poste = models.ForeignKey(Poste, on_delete=models.SET_NULL, null=True, verbose_name="POSTE")
    # Zone = models.ForeignKey(Zone, on_delete=models.SET_NULL, null=True, verbose_name="ZONE")
    Fiche = models.ForeignKey(Fiche, on_delete=models.SET_NULL, null=True, verbose_name="FICHE")

    Statut = models.ForeignKey(Statut, on_delete=models.SET_NULL, null=True, default=1, related_name="Statut_TC")

    idOriginal = models.IntegerField(blank=False, null=False)

    Action = models.CharField(blank=True, max_length=20)
    DateAction = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        ordering = ["-DateAction"]

    def __str__(self):
        return self.Titre


class Commentaire(models.Model):
    Nom = models.CharField(verbose_name="Nom", max_length=55, blank=False)
    # Prenom = models.CharField(verbose_name="Prénom", max_length=55, blank=False)
    DateCreation = models.DateTimeField(auto_now_add=True, null=True)
    DateModification = models.DateTimeField(auto_now=True)
    Titre = models.CharField(max_length=80, blank=False)
    Contenu = models.TextField(blank=False)

    # Poste = models.ForeignKey(Poste, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="POSTE")
    # Zone = models.ForeignKey(Zone, on_delete=models.SET_NULL, null=True, blank=True,  related_name="ZONE")
    Fiche = models.ForeignKey(Fiche, on_delete=models.SET_NULL, null=True, blank=True,  verbose_name="FICHE")

    Statut = models.ForeignKey(Statut, on_delete=models.SET_NULL, null=True, default=1, related_name="Statut_TH")

    # Prioriter = models.ForeignKey(Prioriter, on_delete=models.SET_NULL, null=True, default=3)
    # Historique = models.ForeignKey(CommentaireHistorique, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ["-DateCreation"]

    def __str__(self):
        return self.Titre
