from django.db import models
from ckeditor.fields import RichTextField


class Article(models.Model):
    titre = models.CharField(max_length=200)
    auteur = models.CharField(max_length=50)
    date = models.DateField()
    contenu = RichTextField()

    def __str__(self):
        return self.titre
