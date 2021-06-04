from django.urls import path
from .views import (HomeView, ProcessuView,
EstudoView,AvaliasaunView,ProgramView, ReportView,
SobreIfView, NoticiasDetailView, AnunsiuDetailView,
ContactView,
SobreCafiView,)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('events/<slug:slug>', NoticiasDetailView.as_view(), name= 'noticiasdetails'),
    path('anunsiu/<slug:slug>',AnunsiuDetailView.as_view(), name ='resultado'),
   # path('programas/', ProgramasView.as_view(), name='programas'),
    path('processu/', ProcessuView.as_view(), name='processu'),
    path('estudo/', EstudoView.as_view(), name='estudo'),
    path('avaliasaun/', AvaliasaunView.as_view(), name='avaliasaun'),
    path('programas/', ProgramView.as_view(), name='programa'),
    #path('programas/<slug:slug>', ProgramDetails.as_view(), 'programa_details'), 
    path('report/', ReportView.as_view(), name='report'),
    path('secretariado/', SobreIfView.as_view(), name='sobresgp'),
    path('cafi/', SobreCafiView.as_view(), name = 'cafi'),
    path('contact/', ContactView.as_view(), name='contact')

    
]
