from django.db import models
from tinymce import models as tinymce_models


# from theme.models import Fiche


# Create your models here.
class GMR(models.Model):
    libelle = models.CharField(max_length=30)

    class Meta:
        verbose_name = "GMR"
        ordering = ["libelle"]

    def __str__(self):
        return self.libelle


class TypeClient(models.Model):
    libelle = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Type Client"
        ordering = ["libelle"]

    def __str__(self):
        return self.libelle


class CategorieConsigne(models.Model):
    libelle = models.URLField(max_length=50)

    class Meta:
        verbose_name = "Categorie consigne"
        ordering = ["libelle"]

    def __str__(self):
        return self.libelle


class Consigne(models.Model):
    CategorieConsigne = models.ForeignKey(CategorieConsigne, on_delete=models.SET_NULL, null=True)

    libelle = models.CharField(max_length=100)
    url = models.URLField(blank=True)

    class Meta:
        verbose_name = "Consigne"
        ordering = ["libelle"]

    def __str__(self):
        return self.libelle


class Groupement(models.Model):
    libelle = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Groupement"
        ordering = ["libelle"]

    def __str__(self):
        return self.libelle


class ACR(models.Model):
    libelle = models.CharField(max_length=20)

    class Meta:
        verbose_name = "ACR"
        ordering = ["libelle"]

    def __str__(self):
        return self.libelle


class PO(models.Model):
    libelle = models.CharField(max_length=5)

    class Meta:
        verbose_name = "PO"
        ordering = ["libelle"]

    def __str__(self):
        return self.libelle


class CategorieZone(models.Model):
    libelle = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Categorie Zone"
        ordering = ["libelle"]

    def __str__(self):
        return self.libelle


class JDB(models.Model):
    libelle = models.CharField(max_length=3)

    def __str__(self):
        return self.libelle


class Impact(models.Model):
    libelle = models.CharField(max_length=20)

    def __str__(self):
        return self.libelle


class AutomatismePoste(models.Model):
    libelle = models.CharField(max_length=3)

    def __str__(self):
        return self.libelle


class Filerie(models.Model):
    libelle = models.CharField(max_length=20)

    def __str__(self):
        return self.libelle


class Tension(models.Model):
    libelle = models.CharField(max_length=20)

    def __str__(self):
        return self.libelle


class CCO(models.Model):
    libelle = models.CharField(max_length=5)

    def __str__(self):
        return self.libelle


class ProtectionBarre(models.Model):
    libelle = models.CharField(max_length=15)

    def __str__(self):
        return self.libelle


class TypePoste(models.Model):
    libelle = models.CharField(max_length=10)

    def __str__(self):
        return self.libelle


class Propriete(models.Model):
    libelle = models.CharField(max_length=20)

    def __str__(self):
        return self.libelle

    class Meta:
        ordering = ["libelle"]


class Couleur(models.Model):
    libelle = models.CharField(max_length=20)

    def __str__(self):
        return self.libelle

    class Meta:
        ordering = ["libelle"]


class Formation(models.Model):
    Titre = models.CharField(verbose_name="Titre", max_length=100)
    MaintenuPar = models.CharField(verbose_name="Maintenu Par", max_length=50)
    Actualite = models.TextField(verbose_name="Actualité", blank=False)
    PMC = models.TextField(verbose_name="Participez au maintien competénce du Centre Exploitation", blank=False)
    Fonctionnement = models.TextField(verbose_name="Fonctionnement du maintien en compétence", blank=False)

    def __str__(self):
        return self.Titre


class Theme(models.Model):
    Theme = models.CharField(verbose_name="Thème", max_length=50)
    ModuleFormation = models.CharField(verbose_name="Module de formation", max_length=40)
    QE = models.TextField(verbose_name="Quizz/Exercices", blank=False)
    Outils = models.TextField(blank=False)
    Divers = models.TextField(blank=False)

    def __str__(self):
        return self.Theme


class Poste(models.Model):
    idRTE = models.CharField(max_length=10)
    libelle = models.CharField(max_length=40)
    image = models.ImageField(upload_to='poste', blank=True)

    # schemas_preferentiel = models.TextField(blank=True)
    schemas_preferentiel = tinymce_models.HTMLField(blank=True)
    statut_sp = models.BooleanField(default=False, verbose_name="VÉRIFIER : SCHEMAS PREFERENTIEL")

    autre_particulariter = models.TextField(blank=True)
    statut_ap = models.BooleanField(default=False, verbose_name="VÉRIFIER : AUTRE PARTICULARITER")

    Tension = models.ForeignKey(Tension, on_delete=models.SET_NULL, null=True, verbose_name="TENSION")
    TypePoste = models.ForeignKey(TypePoste, on_delete=models.SET_NULL, null=True, verbose_name="TYPE")
    Propriete = models.ForeignKey(Propriete, on_delete=models.SET_NULL, null=True, verbose_name="PROPRIÉTÉ")

    COULEURS_CHOICES = [
        ('1', 'BLEU'),
        ('2', 'ROUGE'),
        ('3', 'NOIR'),
    ]
    Couleur = models.ForeignKey(Couleur, on_delete=models.SET_NULL, null=True,choices=COULEURS_CHOICES,  verbose_name="Couleur")
    Impact = models.ForeignKey(Impact, on_delete=models.SET_NULL, null=True, verbose_name="IMPACT")

    protectionBarre = models.ForeignKey(ProtectionBarre, on_delete=models.SET_NULL, null=True, blank=True,
                                        verbose_name="PROTECTIONS BARRES")
    CCO = models.ForeignKey(CCO, on_delete=models.SET_NULL, null=True, blank=True)
    Filerie = models.ForeignKey(Filerie, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="FILERIE")
    AutomatismePoste = models.ForeignKey(AutomatismePoste, on_delete=models.SET_NULL, null=True, blank=True,
                                         verbose_name="AUTOMATISME POSTE")
    JDB = models.ForeignKey(JDB, on_delete=models.SET_NULL, null=True, blank=True,
                            verbose_name="CLIENTS RACCORDÉS SUR JDB")
    Groupement = models.ForeignKey(Groupement, on_delete=models.SET_NULL, null=True, verbose_name="GROUPEMENT")

    Consigne = models.ManyToManyField(Consigne, blank=True, verbose_name="CONSIGNE")

    class Meta:
        verbose_name = "Poste électrique"
        verbose_name_plural = "Postes électriques"
        ordering = ["libelle"]

    def __str__(self):
        return self.libelle


class Zone(models.Model):
    libelle = models.CharField(max_length=20)
    presentation = models.TextField(blank=True)
    image = models.ImageField(upload_to='zone', blank=True)

    CategorieZone = models.ForeignKey(CategorieZone, on_delete=models.SET_NULL, null=True)
    PO = models.ForeignKey(PO, on_delete=models.SET_NULL, null=True)
    GMR = models.ForeignKey(GMR, on_delete=models.SET_NULL, null=True, related_name="GMR_Zone")

    Groupement = models.ManyToManyField(Groupement, related_name="Groupement_Zone")
    ACR = models.ManyToManyField(ACR, blank=False)
    Poste = models.ManyToManyField(Poste, blank=True)

    class Meta:
        verbose_name = "Zone"
        ordering = ["libelle"]

    def __str__(self):
        return self.libelle


class Client(models.Model):
    libelle = models.CharField(max_length=50)

    TypeClient = models.ForeignKey(TypeClient, on_delete=models.SET_NULL, null=True)
    GMR = models.ForeignKey(GMR, on_delete=models.SET_NULL, null=True)
    Poste = models.ManyToManyField(Poste)

    class Meta:
        verbose_name = "Clients raccordés sur JDB"
        ordering = ["libelle"]

    def __str__(self):
        return self.libelle


class Statut(models.Model):
    libelle = models.CharField(max_length=15)

    def __str__(self):
        return self.libelle

    # class Prioriter(models.Model):
    # libelle = models.CharField(max_length=15)

    # def __str__(self):
    #    return self.libelle


class CommentaireHistorique(models.Model):
    Nom = models.CharField(verbose_name="Nom", max_length=50, blank=False)
    # Prenom = models.CharField(verbose_name="Prénom", max_length=50, blank=False)
    Date = models.DateTimeField(null=True, blank=True)
    Titre = models.CharField(max_length=80, blank=False)
    Contenu = models.TextField(blank=False)

    Poste = models.ForeignKey(Poste, on_delete=models.SET_NULL, null=True, verbose_name="POSTE")
    # Zone = models.ForeignKey(Zone, on_delete=models.SET_NULL, null=True, verbose_name="ZONE")
    # Fiche = models.ForeignKey(Fiche, on_delete=models.SET_NULL, null=True, verbose_name="FICHE")

    Statut = models.ForeignKey(Statut, on_delete=models.SET_NULL, null=True, default=1)

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

    Poste = models.ForeignKey(Poste, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="POSTE")
    # Zone = models.ForeignKey(Zone, on_delete=models.SET_NULL, null=True, blank=True,  related_name="ZONE")
    # Fiche = models.ForeignKey(Fiche, on_delete=models.SET_NULL, null=True, blank=True,  verbose_name="FICHE")

    Statut = models.ForeignKey(Statut, on_delete=models.SET_NULL, null=True, default=1)

    # Prioriter = models.ForeignKey(Prioriter, on_delete=models.SET_NULL, null=True, default=3)
    # Historique = models.ForeignKey(CommentaireHistorique, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ["-DateCreation"]

    def __str__(self):
        return self.Titre


class User(models.Model):
    Nom = models.CharField(max_length=30)
    Prenom = models.CharField(max_length=30)

    def __str__(self):
        return self.Nom
