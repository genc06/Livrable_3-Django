from django.shortcuts import render
from models import Exercice
from models import Categorie
from models import CategorieExercice

def test(request):
    exercices = Exercice.objects.all()
    return render(request, 'Liv3_base.html', {'exercices': exercices})

