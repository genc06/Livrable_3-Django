"""
URL configuration for Musculation project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ExercicesMusculation.Exercices import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('categories/', views.afficheCategorie, name='categories'),

    # URL pour ajouter une nouvelle catégorie
    path('categories/add/', views.add_category, name='add_category'),

    # URL pour supprimer une catégorie existante
    path('categories/delete/<int:category_id>/', views.delete_category, name='delete_category'),

    # URL pour mettre à jour une catégorie existante
    path('categories/update/<int:category_id>/', views.update_category, name='update_category'),
]


