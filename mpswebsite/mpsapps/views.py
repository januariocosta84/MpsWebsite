from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.http import HttpResponse
from django.utils.translation import gettext as _
from .models import (FundoModel, SgpModel,
                    Noticias, Anunsiu, SgpStaff,
                    CafiMembro,PorcesuPagamento,
                    EstudoViabialidade,Avaliasaun, Programas, InfoProgramas)
class HomeView(TemplateView):
    template_name ='mpsapps/home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['home_test'] = FundoModel.objects.all()
        context['noticias'] = Noticias.objects.all()
        context['anunsius'] = Anunsiu.objects.all()
        return context

class NoticiasDetailView(DetailView):
    """Noticias details view"""
    context_object_name = 'noticiasview'
    model = Noticias
    template_name = 'mpsapps/noticiadetails.html' 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['noticias'] =Noticias.objects.all()
        return context

class AnunsiuDetailView(DetailView):
    """Anunsiu Details View"""
    context_object_name = 'anunsiu_details'
    model = Anunsiu
    template_name = 'mpsapps/anunsiu-details.html'

class SobreIfView(TemplateView):
    """SobreIFView"""
    template_name = 'mpsapps/sobresgp.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sobre_sgp'] = SgpModel.objects.get(id=2)
        context['staff_sgp'] = SgpStaff.objects.all()
        return context

class SobreCafiView(TemplateView):
    """Kona ba CAFI ho nia membro sira"""
    template_name = 'mpsapps/sobrefundo.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sobre_cafi'] = FundoModel.objects.get(id=2)
        context['membro_cafi'] = CafiMembro.objects.all()
        return context

class ProcessuView(TemplateView):
    template_name='mpsapps/processo.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if True:
            context['procesu_pagamento'] = PorcesuPagamento.objects.get(id=1)
        return context

class EstudoView(TemplateView):
    template_name='mpsapps/estudoviabilidade.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if context:
            context['estudo_viabilidade'] = EstudoViabialidade.objects.get(id=2)
        return context

class AvaliasaunView(TemplateView):
    template_name = 'mpsapps/avaliasaun.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['apraise'] = Avaliasaun.objects.all()
        return context


class ProgramView(TemplateView):

    template_name='mpsapps/programa.html'
    def get_context_data(self, **kwagrs):
        context = super().get_context_data(**kwagrs)
        context['programas'] = Programas.objects.all()
        try:
            context['info_programas'] = InfoProgramas.objects.get(id=1)
        except ObjectDoesNotExist:
            return print('the error is')
        return context

class ReportView(TemplateView):
    template_name = 'mpsapps/under_construction.html'

class ContactView(TemplateView):
    template_name = 'mpsapps/under_construction.html'