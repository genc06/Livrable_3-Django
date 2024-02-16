from django.shortcuts import render, redirect
from .models import Exercice, Categorie
from django.http import HttpResponse

def afficheExercices(request):
    exercices = Exercice.objects.all()
    return render(request, 'Liv3_base.html', {'exercices': exercices})

def afficheCategorie(request):
    categories = Categorie.objects.all()
    return render(request, 'Liv3_base.html', {'categories': categories})

def delete_category(request, category_id):
    if request.method == 'POST':
        category = Categorie.objects.get(pk=category_id)
        category.delete()
        return redirect('categories')
    else:
        return HttpResponse("Method Not Allowed", status=405)

def update_category(request, category_id):
    if request.method == 'POST':
        updated_name = request.POST.get('updated_name')
        category = Categorie.objects.get(pk=category_id)
        category.nom = updated_name
        category.save()
        return redirect('categories')
    else:
        return HttpResponse("Method Not Allowed", status=405)

def add_category(request):
    if request.method == 'POST':
        new_category_name = request.POST.get('new_category_name')
        category = Categorie(nom=new_category_name)
        category.save()
        return redirect('categories')
    else:
        return HttpResponse("Method Not Allowed", status=405)
