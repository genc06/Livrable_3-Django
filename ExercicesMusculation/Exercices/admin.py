from django.contrib import admin
from .models import Exercice, Categorie, CategorieExercice


admin.site.register(Exercice)
admin.site.register(Categorie)
admin.site.register(CategorieExercice)

