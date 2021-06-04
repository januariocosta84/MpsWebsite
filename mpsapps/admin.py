from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import (FundoModel, SgpModel,
                     Noticias, Anunsiu, 
                     SgpStaff,CafiMembro, 
                     PorcesuPagamento,EstudoViabialidade,Avaliasaun, Programas, InfoProgramas)

# Register your models here.

class FundoModelAdmin(admin.ModelAdmin):
    list_display =['title']
    prepopulated_fields = {'slug':('title',)}

class SgpModelAdmin(admin.ModelAdmin):
    list_display = ['title']
    prepopulated_fields = {'slug': ('title',)}

class NoticiasAdmin(admin.ModelAdmin):
    list_display = ['title']
    prepopulated_fields ={'slug':('title',)}
"""
Tuir mai Dashboard ba Tradusaun nia 
"""
class AnunsiuAdmin(TranslationAdmin):
    list_display = ['title']
    prepopulated_fields ={'slug':('title',)}
class NoticiasAdmin(TranslationAdmin):
    list_display =['title']
    prepopulated_fields ={'slug':('title',)}
class SgpStaffAdmin(TranslationAdmin):
    list_display =['title']
class FundoAdmin(TranslationAdmin):
    list_display =['title']
    prepopulated_fields ={'slug':('title',)}
class SGPadmin(TranslationAdmin):
    list_display =['title']
    prepopulated_fields ={'slug':('title',)}
class ProgramasAdmin(TranslationAdmin):
    list_display = ['title']
    prepopulated_fields ={'slug':('title',)}
class ProgramsInfoAdmin(TranslationAdmin):
    list_display =['title']

admin.site.register(FundoModel)
admin.site.register(CafiMembro)
admin.site.register(SgpStaff)
admin.site.register(SgpModel, SgpModelAdmin)
admin.site.register(Noticias,NoticiasAdmin)
admin.site.register(Anunsiu, AnunsiuAdmin)
admin.site.register(PorcesuPagamento)
admin.site.register(EstudoViabialidade)
admin.site.register(Avaliasaun)
admin.site.register(Programas)
admin.site.register(InfoProgramas)