from django.shortcuts import render

def glowna(request):
    return render(request, 'sterownik_piec/glowna.html', {})