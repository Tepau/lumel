from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class Article(models.Model):
    titre = models.CharField(max_length=200)
    auteur = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)
    contenu = CKEditor5Field('Contenu', config_name='extends')

    def __str__(self):
        return self.titre
