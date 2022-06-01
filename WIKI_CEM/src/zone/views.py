from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

from django.views.generic import ListView, CreateView, DetailView, UpdateView

from poste.models import CategorieZone, Zone
from poste.models import Poste, Commentaire
from zone.models import Commentaire, CommentaireHistorique
from zone.forms import zoneForm


class ZoneHome(ListView):
    model = CategorieZone
    template_name = 'zone/ZoneHome.html'
    context_object_name = "Catzone"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['C'] = Zone.objects.filter(CategorieZone=self.kwargs['pk'])

        context['Cat'] = CategorieZone.objects.all()  # pour récupérer toutes les Categories de zones
        context['Z'] = Zone.objects.all().order_by('CategorieZone__id')  # pour récupérer toutes les zones classées par
        # ordre ascendant des id de 'CategorieZone'
        # à tester aussi
        for c in context['Cat']:
            context['C' + str(c.id)] = Zone.objects.filter(CategorieZone=c)  # pour générr un context['Cx']
            # correpondant à la CategorieZone x

        return context


class ZoneHomeCategorieZone(DetailView):
    model = Zone
    template_name = 'zone/ZoneDetail.html'
    context_object_name = "zone"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['C'] = Commentaire.objects.filter(Zone=self.kwargs['pk'])
        return context


class CommentCreateZoneView(CreateView):
    model = Commentaire
    template_name = 'poste/create_comment.html'
    # fields = ['Zone', 'Nom', 'Prenom', 'Titre', 'Contenu']
    form_class = zoneForm

    # success_url = reverse_lazy('zone:Zone-Home')

    def get_success_url(self):
        # Commentaire.objects.filter(Poste=self.kwargs['pk'])
        return reverse_lazy("zone:Zone-detail", kwargs={'pk': self.object.Zone_id})

    def get_initial(self):
        initial = super(CommentCreateZoneView, self).get_initial()
        # cpf - it's the name of the field on your current form
        # self.args will be filled from URL. I'd suggest to use named parameters
        # so you can access e.g. self.kwargs['cpf_initial']
        initial['Zone'] = self.kwargs['pk']
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['submit_text'] = "CRÉER CONTENU"
        context['titre'] = "CRÉATION D'UN CONTENU"
        return context


class CommentUpdateZoneView(UpdateView):
    model = Commentaire
    template_name = 'poste/create_comment.html'
    form_class = zoneForm
    # fields = ['Poste', 'Nom', 'Prenom', 'Titre', 'Contenu']

    def get_success_url(self):
        # Commentaire.objects.filter(Poste=self.kwargs['pk'])
        return reverse_lazy("zone:Zone-detail", kwargs={'pk': self.object.Zone_id})

    def form_valid(self, form):
        # form.instance.Statut = Statut.objects.get(pk=int(1))
        # form.instance.Nom = Statut.objects.get(pk=int(1))
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['submit_text'] = "MODIFIER CONTENU"
        context['titre'] = "MODIFICATION D'UN CONTENU"
        return context


class HistoriqueZone(ListView):
    model = CommentaireHistorique
    template_name = 'zone/zone_historique_commentaire.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Actuel'] = Commentaire.objects.filter(pk=self.kwargs['pk'])
        context['Historique'] = CommentaireHistorique.objects.filter(idOriginal=self.kwargs['pk'])

        return context

