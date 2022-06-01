from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

from django.views.generic import ListView, CreateView, DetailView, UpdateView

from theme.models import Fiche, Commentaire, CommentaireHistorique
from poste.models import Statut


from theme.forms import ficheForm


class ThemeHome(ListView):
    queryset = Fiche.objects.filter(TypeFiche="1")
    template_name = 'theme/theme.html'
    context_object_name = "theme"


class ModopHome(ListView):
    queryset = Fiche.objects.filter(TypeFiche="2")
    template_name = 'modop/modop_acc.html'
    context_object_name = "modop"


class ThemeFiche(DetailView):
    model = Fiche
    template_name = 'theme/theme-detail.html'
    context_object_name = "theme_detail"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['C'] = Commentaire.objects.filter(Fiche=self.kwargs['pk'])
        return context


class ModopFiche(DetailView):
    model = Fiche
    template_name = 'modop/modop_detail.html'
    # template_name = 'theme/theme-detail.html'
    context_object_name = "modop_detail"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['C'] = Commentaire.objects.filter(Fiche=self.kwargs['pk'])
        return context


class CommentCreateViewTheme(CreateView):
    model = Commentaire
    template_name = 'poste/create_comment.html'
    form_class = ficheForm

    # fields = ['Fiche', 'Nom', 'Prenom', 'Titre', 'Contenu']
    # success_url = reverse_lazy('theme:Theme')

    def get_success_url(self):
        return reverse_lazy("theme:Theme-detail", kwargs={'pk': self.object.Fiche_id})

    def get_initial(self):
        initial = super(CommentCreateViewTheme, self).get_initial()
        # cpf - it's the name of the field on your current form
        # self.args will be filled from URL. I'd suggest to use named parameters
        # so you can access e.g. self.kwargs['cpf_initial']
        initial['Fiche'] = self.kwargs['pk']
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['submit_text'] = "CRÉER CONTENU"
        context['titre'] = "CRÉATION CONTENU"

        # context['Fiche'] = self.kwargs['pk']
        # context['RT'] = "'theme:Theme-detail' pk="

        return context


class CommentUpdateViewTheme(UpdateView):
    model = Commentaire
    template_name = 'theme/create_comment_theme.html'
    form_class = ficheForm

    def get_success_url(self):
        # Commentaire.objects.filter(Poste=self.kwargs['pk'])
        return reverse_lazy("theme:Theme-detail", kwargs={'pk': self.object.Fiche_id})

    def form_valid(self, form):
        form.instance.Statut = Statut.objects.get(pk=int(1))
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['submit_text'] = "MODIFIER CONTENU"
        context['titre'] = "MODIFICATION DU CONTENU"
        return context


class Historique(ListView):
    model = CommentaireHistorique
    template_name = 'theme/theme_historique_commentaire.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Actuel'] = Commentaire.objects.filter(pk=self.kwargs['pk'])
        context['Historique'] = CommentaireHistorique.objects.filter(idOriginal=self.kwargs['pk'])

        return context
