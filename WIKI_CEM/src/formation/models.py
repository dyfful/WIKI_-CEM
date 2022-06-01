from django.db import models


# Create your models here.
class Doc(models.Model):
    libelle = models.CharField(max_length=50)
    url = models.URLField(max_length=600)
    nomButton = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Doc"
        ordering = ["libelle"]

    def __str__(self):
        return self.libelle


class Footer(models.Model):
    Titre = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Titre pied de page"
        ordering = ["Titre"]

    def __str__(self):
        return self.Titre


class Lien(models.Model):
    nom = models.CharField(max_length=50)
    url = models.URLField(max_length=600)

    class Meta:
        verbose_name = "Lien utile"
        ordering = ["nom"]

    def __str__(self):
        return self.nom
