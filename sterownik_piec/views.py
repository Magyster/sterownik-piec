from django.shortcuts import render
from django.http import JsonResponse
from .models import Czujniki
import json
import datetime

def glowna(request):
    czujniki = Czujniki.objects.all()
    dane = {}
    teraz = datetime.datetime.now()
    data = teraz.date()
    czas = teraz.time()
    dane['data'] = data
    dane['czas'] = czas
    for czujnik in czujniki:
        if(czujnik.typ == 'T'):
            dane[czujnik.nazwa] =  round(czujnik.wartosc,1)#Czujniki.objects.filter(nazwa='T_dom_A')
        else:
            dane[czujnik.nazwa] =  int(czujnik.wartosc)
        
    return render(request, 'sterownik_piec/glowna.html', dane)

def zapis_do_bazy(request):
    if request.method == 'POST':
        #zapis wartości dla przesłanych czujników
        czujniki = json.loads(request.body)
        for klucz, wartosc in czujniki.items():
            czujnik = Czujniki.objects.get(nazwa = klucz)
            czujnik.wartosc = wartosc
            czujnik.save()
        #obliczenie tem zadanej grzejników
        czujnik = Czujniki.objects.get(nazwa = 'T_grzejniki_Z')
        t_dom = Czujniki.objects.get(nazwa='T_dom_A')
        t_zewnetrzna = Czujniki.objects.get(nazwa='T_zewnetrzna_A')
        wartosc = (-1 * t_dom.wartosc + 85) - t_zewnetrzna.wartosc
        czujnik.wartosc = wartosc
        czujnik.save()
    return JsonResponse(None, safe=False)

def odczyt_z_bazy(request):
    czujniki = Czujniki.objects.all()
    dane = {}
    for czujnik in czujniki:
        dane.update({czujnik.nazwa:czujnik.wartosc})        
    return JsonResponse(dane, safe=False)