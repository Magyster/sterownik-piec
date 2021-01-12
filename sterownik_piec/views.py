from django.shortcuts import render, reverse
from django.http import JsonResponse
from django.views import View
from .models import Czujniki
import json
import datetime

class Glowna(View):

    def get(self, request):
        czujniki = Czujniki.objects.all()
        dane = {}
        teraz = datetime.datetime.now()
        data = teraz.date()
        czas = teraz.time()
        dane['data'] = data
        dane['czas'] = czas
        for czujnik in czujniki:
            if(czujnik.typ == 'T'):
                dane[czujnik.nazwa] =  round(czujnik.wartosc,1)
            else:
                dane[czujnik.nazwa] =  int(czujnik.wartosc)        
        return render(request, 'sterownik_piec/glowna.html', dane)

    def post(self, request):
        czujniki = request.POST        
        for klucz, wartosc in czujniki.items():
            if(klucz != 'csrfmiddlewaretoken'):
                czujnik = Czujniki.objects.get(nazwa = klucz)
                czujnik.wartosc = wartosc
                czujnik.save()

        czujniki = Czujniki.objects.all()
        dane = {}
        teraz = datetime.datetime.now()
        data = teraz.date()
        czas = teraz.time()
        dane['data'] = data
        dane['czas'] = czas
        for czujnik in czujniki:
            if(czujnik.typ == 'T'):
                dane[czujnik.nazwa] =  round(czujnik.wartosc,1)
            else:
                dane[czujnik.nazwa] =  int(czujnik.wartosc)        
        return render(request, 'sterownik_piec/glowna.html', dane)


class ZapisDoBazy(View):

    def get(self, request):
        pass        

    def post(self, request):
        #zapis wartości dla przesłanych czujników
        czujniki = json.loads(request.body)
        for klucz, wartosc in czujniki.items():
            czujnik = Czujniki.objects.get(nazwa = klucz)
            czujnik.wartosc = wartosc
            czujnik.save()
        #obliczenie temperatury zadanej grzejników
        czujnik = Czujniki.objects.get(nazwa = 'T_grzejniki_Z')
        t_dom = Czujniki.objects.get(nazwa='T_dom_A')
        t_zewnetrzna = Czujniki.objects.get(nazwa='T_zewnetrzna_A')
        wartosc = 60 + (23 - t_dom.wartosc) - t_zewnetrzna.wartosc / 2
        czujnik.wartosc = wartosc
        czujnik.save()
        return JsonResponse(None, safe=False)


class OdczytZBazy(View):

    def get(self, request):
        czujniki = Czujniki.objects.all()
        dane = {}
        for czujnik in czujniki:
            dane.update({czujnik.nazwa:czujnik.wartosc})        
        return JsonResponse(dane, safe=False)

    def post(self, request):
        pass