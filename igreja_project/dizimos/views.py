from django.shortcuts import render
from .models import Fiel, Dizimo

def index(request):
    fieis = Fiel.objects.all()
    return render(request, 'index.html', {{ 'fieis': fieis }})
