from django.shortcuts import render
from .models import Czujniki

def glowna(request):
    czujniki = Czujniki.objects.all()
    #czujniki = Czujniki.objects.filter(nazwa='T_dom_A')
    return render(request, 'sterownik_piec/glowna.html', {'czujniki':czujniki})