import ctypes
import json

from django.core.paginator import Page
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse

from django.views.generic import ListView, CreateView, DetailView, UpdateView

from poste.models import Poste, User, Commentaire, Zone, Statut, CommentaireHistorique
from poste.forms import Com, Post
from django.db.models import Q

import os;

from psycopg2.extensions import JSON


class Home(ListView):
    model = Poste
    context_object_name = "poste"


class showList(ListView):
    model = Poste
    template_name = 'poste/sb.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sB'] = Poste.objects.all()
        return context


class PosteSearch(ListView):
    model = Poste
    template_name = 'poste/poste_search.html'


# Poste recherche par alphabet
class PosteRT(ListView):
    model = Poste
    template_name = 'poste/poste_searchRT.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['C'] = Poste.objects.filter(libelle__istartswith=self.kwargs['lettreRechercher'])
        return context


class PosteP(DetailView):
    model = Poste
    template_name = 'poste/poste_searchP.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Zone'] = Zone.objects.filter(Poste=self.kwargs['pk'])
        context['C'] = Commentaire.objects.filter(Poste=self.kwargs['pk'])

        # context['U'] = os.environ.get("USERNAME")
        # context['U1'] = os.environ.get("USER")

        return context


class CommentCreateView(CreateView):
    model = Commentaire
    template_name = 'poste/create_comment.html'
    form_class = Com

    # form = Test()
    # fields = ['Poste', 'Nom', 'Prenom', 'Titre', 'Contenu']
    # form = Com()

    def get_success_url(self):
        # Commentaire.objects.filter(Poste=self.kwargs['pk'])
        return reverse_lazy("poste:PosteP", kwargs={'pk': self.object.Poste_id})

    # def get_absolute_url(self):
    # return reverse_lazy('poste:PosteP', kwargs={'pk': self.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['submit_text'] = "CRÉER CONTENU"
        context['titre'] = "CRÉATION D'UN CONTENU"
        return context

    def get_initial(self):
        initial = super(CommentCreateView, self).get_initial()
        # cpf - it's the name of the field on your current form
        # self.args will be filled from URL. I'd suggest to use named parameters
        # so you can access e.g. self.kwargs['cpf_initial']

        GetUserNameEx = ctypes.windll.secur32.GetUserNameExW
        NameDisplay = 3

        size = ctypes.pointer(ctypes.c_ulong(0))
        GetUserNameEx(NameDisplay, None, size)

        nameBuffer = ctypes.create_unicode_buffer(size.contents.value)
        GetUserNameEx(NameDisplay, nameBuffer, size)

        initial['Poste'] = self.kwargs['pk']
        # initial['Prenom'] = nameBuffer.value
        return initial


class CommentUpdateView(UpdateView):
    model = Commentaire
    template_name = 'poste/create_comment.html'
    form_class = Com

    # fields = ['Poste', 'Nom', 'Prenom', 'Titre', 'Contenu']

    def get_success_url(self):
        # Commentaire.objects.filter(Poste=self.kwargs['pk'])
        return reverse_lazy("poste:PosteP", kwargs={'pk': self.object.Poste_id})

    def form_valid(self, form):
        # form.instance.Statut = Statut.objects.get(pk=int(1))
        # form.instance.Nom = Statut.objects.get(pk=int(1))
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['submit_text'] = "MODIFIER CONTENU"
        context['titre'] = "MODIFICATION D'UN CONTENU"
        return context


class SchemaPreferentielUpdateView(UpdateView):
    model = Poste
    template_name = 'poste/create_comment.html'
    fields = ['schemas_preferentiel']

    def get_success_url(self):
        return reverse_lazy("poste:PosteP", kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.statut_sp = False
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['submit_text'] = "MODIFIER SCHÉMAS PRÉFÉRENTIEL"
        context['titre'] = "MODIFICATION CONTENU"
        return context


class AutreParticulariterUpdateView(UpdateView):
    model = Poste
    template_name = 'poste/create_comment.html'
    fields = ['autre_particulariter']

    def get_success_url(self):
        return reverse_lazy("poste:PosteP", kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.statut_ap = False
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['submit_text'] = "MODIFICATION CONTENU"
        context['titre'] = "MODIFIER AUTRE PARTICULARITER"
        return context


class PosteUpdateView(UpdateView):
    model = Poste
    template_name = 'poste/poste_update_form.html'
    form_class = Post

    # fields = ['Poste', 'Nom', 'Prenom', 'Titre', 'Contenu']

    def get_success_url(self):
        # Commentaire.objects.filter(Poste=self.kwargs['pk'])
        return reverse_lazy("poste:PosteP", kwargs={'pk': self.object.id})

    def form_valid(self, form):
        # form.instance.Statut = Statut.objects.get(pk=int(1))
        # form.instance.Nom = Statut.objects.get(pk=int(1))
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['submit_text'] = "MODIFIER INFORMATION POSTE"
        context['titre'] = "MODIFICATION DU POSTE"
        return context


class Historique(ListView):
    model = CommentaireHistorique
    template_name = 'poste/poste_historique_commentaire.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Actuel'] = Commentaire.objects.filter(pk=self.kwargs['pk'])
        context['Historique'] = CommentaireHistorique.objects.filter(idOriginal=self.kwargs['pk'])

        return context


# class SupprimerCommentaire(ListView):
#     model = Commentaire
#     template_name = 'poste/poste_searchP.html'
#
#     def get_success_url(self):
#         return reverse_lazy("poste:PosteP", kwargs={'pk': self.object.Poste_id})
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['Actuel'] = Commentaire.objects.filter(pk=self.kwargs['pk']).update(Statut=3)
#
#         return context

def SupprimerCommentaire(request, **kwargs):
    toChange = Commentaire.objects.filter(pk=kwargs['pk']).update(Statut=3)
    # toChange = Commentaire.objects.filter(pk=kwargs['pk']).update(Statut=3)
    # print(f'{toChange = }')
    # print(toChange)
    # print('toChange', toChange)
    # return render(request, 'poste/poste_searchP.html', {})
    # return JsonResponse({'statut': 200})
    # return render(request, 'poste/searchP.html', {'poll': p})
    # return HttpResponseRedirect(reverse('PosteP',  kwargs={'pk': toChange.Poste_id}))
    return redirect(request.META['HTTP_REFERER'])


# /search/?adress=
def search_poste(request):
    libelle = request.GET.get('nom')
    payload = list()
    if libelle:
        poste_obj = Poste.objects.filter(libelle__icontains=libelle)

        for p_o in poste_obj:
            # data = {}
            data = {'id': p_o.id, 'libelle': p_o.libelle, 'tension': p_o.Tension.libelle}
            payload.append(data)
    return JsonResponse({'status': 200, 'data': payload})


# def autocomplete(request):
#     print(request.GET)
#     if "term" in request.GET:
#         qs = User.objects.filter(Q(Nom__icontains=request.GET.get('term')) | Q(Prenom__icontains=request.GET.get('term')))
#         payload = list()
#         for user in qs:
#             payload.append(user.Nom + " " + user.Prenom)
#         return JsonResponse(payload, safe=False)


def autocomplete(request):
    if "term" in request.GET:
        qs = User.objects.filter(
            Q(Nom__icontains=request.GET.get('term')) | Q(Prenom__icontains=request.GET.get('term')))
        rt = []
        for user in qs:
            data = {}
            data['label'] = user.Nom + " " + user.Prenom
            # data['value'] = user.id
            rt.append(data)
        return JsonResponse(rt, safe=False)
