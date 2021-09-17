from django.conf import settings
from django.utils.translation import gettext_lazy
from modeltranslation.translator import translator, register, TranslationOptions
from .models import (Anunsiu, Noticias, 
SgpStaff, FundoModel,Programas,
SgpModel, PorcesuPagamento,EstudoViabialidade, CafiMembro, InfoProgramas, Avaliasaun)

class TraduzAnunsiu(TranslationOptions):
    fields =('title', 'konteudu')
translator.register(Anunsiu, TraduzAnunsiu)

class TraduzNoticias(TranslationOptions):
    fields =('title', 'konteudu')
translator.register(Noticias, TraduzNoticias)

class TraduzSgpStaff(TranslationOptions):
    fields =('title',)
translator.register(SgpStaff, TraduzSgpStaff)

class TraduzCafiMember(TranslationOptions):
    fields=('title','cargo')
translator.register(CafiMembro, TraduzCafiMember)

class TraduzFundo(TranslationOptions):
    fields =('title','konteudu')
translator.register(FundoModel, TraduzFundo)

class TraduzSGP(TranslationOptions):
    fields =('title','konteudu')
translator.register(SgpModel, TraduzSGP)

class TraduzProcessPagamento(TranslationOptions):
    fields = ('title', 'konteudu')
translator.register(PorcesuPagamento, TraduzProcessPagamento)

class TraduzEstuduViabilidade(TranslationOptions):
    fields = ('title','konteudu')
translator.register(EstudoViabialidade, TraduzEstuduViabilidade)

class TraduzProgramas(TranslationOptions):
    fields = ('title', 'konteudu')
translator.register(Programas, TraduzProgramas)

class TraduzInfoPrograms(TranslationOptions):
    fields =('title', 'konteudu')
translator.register(InfoProgramas, TraduzInfoPrograms)

class TraduzAvaliasaun(TranslationOptions):
    fields =('title', 'konteudu')
translator.register(Avaliasaun, TraduzAvaliasaun)