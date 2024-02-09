
from django.shortcuts import render
from .models import Exercice, Categorie
from .models import CategorieExercice



def test(request):
    exercices = Exercice.objects.all()
    return render(request, 'Liv3_base.html', {'exercices': exercices})


def afficheCategorie(request):
    categories = Categorie.objects.all()
    return render(request, 'Liv3_categorie.html', {'categories': categories})