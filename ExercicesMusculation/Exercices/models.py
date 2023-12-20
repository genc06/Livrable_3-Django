from django.db import models

# Create your models here.
from django.db import models

class Categorie(models.Model):
    nom = models.CharField(max_length=25)

    def __str__(self):
        return self.nom

class Exercice(models.Model):
    nom = models.CharField(max_length=100)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nom