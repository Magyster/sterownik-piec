from django.shortcuts import render
from django.http import JsonResponse
from .models import Czujniki
import json
import datetime

def glowna(request):
    czujniki = Czujniki.objects.all()
    teraz = datetime.datetime.now()
    data = teraz.date()
    czas = teraz.time()
    for czujnik in czujniki:
        if czujnik.nazwa == 'T_dom_A':
            czujnik_T_dom_A = czujnik.wartosc#Czujniki.objects.filter(nazwa='T_dom_A')
        if czujnik.nazwa == 'W_dom_A':
            czujnik_W_dom_A = int(czujnik.wartosc)
        if czujnik.nazwa == 'C_dom_A':
            czujnik_C_dom_A = int(czujnik.wartosc)
        if czujnik.nazwa == 'T_bojler_A':
            czujnik_T_bojler_A = czujnik.wartosc
        if czujnik.nazwa == 'T_piec_A':
            czujnik_T_piec_A = czujnik.wartosc
        if czujnik.nazwa == 'T_grzejniki_A':
            czujnik_T_grzejniki_A = czujnik.wartosc
    return render(request, 'sterownik_piec/glowna.html', { 'data':data, 'czas':czas, 'czujnik_T_dom_A':czujnik_T_dom_A, 'czujnik_W_dom_A':czujnik_W_dom_A, 'czujnik_C_dom_A':czujnik_C_dom_A,'czujnik_T_bojler_A':czujnik_T_bojler_A, 'czujnik_T_piec_A':czujnik_T_piec_A, 'czujnik_T_grzejniki_A':czujnik_T_grzejniki_A,})

def zapis_do_bazy(request):
    if request.method == 'POST':
        czujniki = json.loads(request.body)
        for klucz, wartosc in czujniki.items():
            czujnik = Czujniki.objects.get(nazwa = klucz)
            czujnik.wartosc = wartosc
            czujnik.save()
    return JsonResponse(None, safe=False)

def odczyt_z_bazy(request):
    czujniki = Czujniki.objects.all()
    dane = {}
    for czujnik in czujniki:
        dane.update({czujnik.nazwa:czujnik.wartosc})        
    return JsonResponse(dane, safe=False)