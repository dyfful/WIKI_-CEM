from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

from django.views.generic import ListView, CreateView, DetailView, UpdateView

from formation.models import Doc, Footer, Lien


class FormationHome(ListView):
    model = Doc
    template_name = 'formation/FormationHome.html'
    context_object_name = "formation"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Footer'] = Footer.objects.all()
        context['Lien'] = Lien.objects.all()
        # context['Doc'] = Doc.objects.all()

        return context


class FormationHomeInfo(ListView):
    model = Doc
    template_name = 'formation/FormationHomeInfo.html'
    context_object_name = "formation"



