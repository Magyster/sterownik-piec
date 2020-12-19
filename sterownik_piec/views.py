from django.shortcuts import render
from .models import Czujniki

def glowna(request):
    czujniki = Czujniki.objects.all()
    for czujnik in czujniki:
        if czujnik.nazwa == 'T_dom_A':
            czujnik_T_dom_A = czujnik.wartosc#Czujniki.objects.filter(nazwa='T_dom_A')
    return render(request, 'sterownik_piec/glowna.html', {'czujnik_T_dom_A':czujnik_T_dom_A,})