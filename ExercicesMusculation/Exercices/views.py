from django.shortcuts import render
from models import *
# Create your views here.


def test(request):
    exercice = Exercice.object.all()

