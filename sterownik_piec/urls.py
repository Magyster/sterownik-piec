from django.urls import path
from . import views

urlpatterns = [
    path('', views.glowna, name='glowna'),
    path('zapisdobazy/', views.zapis_do_bazy, name='zapis_do_bazy'),
    path('odczytzbazy/', views.odczyt_z_bazy, name='odczyt_z_bazy'),
]