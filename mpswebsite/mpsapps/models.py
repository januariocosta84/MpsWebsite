from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

cargo_membro= [
    ('presidente', 'presidente'),
    ('membru', 'membru'),
    ('presidente', 'presidente'),
    ('membro', 'membro'),
    ('president', 'president'),
    ('member', 'member'),
]


class FundoModel(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    konteudu = RichTextUploadingField()

    def __str__(self):
        return self.title


class SgpModel(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    konteudu = RichTextUploadingField()

    def __str__(self):
        return self.title

class CafiMembro(models.Model):
    naran = models.CharField(max_length=50);
    title = models.CharField(max_length=50)
    cargo = models.CharField(max_length=50,choices=cargo_membro, blank=True)
    image = models.ImageField(upload_to='membro_cafi')
    status = models.BooleanField()

    def __str__(self):
        return self.naran

class SgpStaff(models.Model):
    naran = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='staff', blank=True)
    status = models.BooleanField()

    def __str__(self):
        return self.naran

class Noticias(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='noticias')
    konteudu =RichTextUploadingField()
    data = models.DateField()
    def __str__(self):
        return self.title

class Anunsiu(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to = 'anunsiu',)
    konteudu = RichTextUploadingField()
    data = models.DateField()

    def __str__(self):
        return self.title

class PorcesuPagamento(models.Model):
    title = models.CharField(max_length=50)
    konteudu = RichTextUploadingField()

    def __str__(self):
        return self.title

class EstudoViabialidade(models.Model):
    title = models.CharField(max_length=50)
    konteudu = RichTextUploadingField()

    def __str__(self):
        return self.title

class Avaliasaun(models.Model):
    title = models.CharField(max_length=50)
    konteudu = RichTextUploadingField()

    def __str__(self):
        return self.title


class Programas(models.Model):
    title = models.CharField(max_length =50)
    slug = models.SlugField(unique=True)
    konteudu = RichTextUploadingField()
    image = models.ImageField(upload_to ='programas')

    def __str__(self):
        return self.title

class InfoProgramas(models.Model):
    title = models.CharField(max_length=50);
    konteudu =RichTextUploadingField()

    def __str__(self):
        return self.title