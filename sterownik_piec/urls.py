from django.urls import path
from . import views

urlpatterns = [
    path('', views.Glowna.as_view(), name='Glowna'),
    path('ZapisDoBazy/', views.ZapisDoBazy.as_view(), name='ZapisDoBazy'),
    path('OdczytZBazy/', views.OdczytZBazy.as_view(), name='OdczytZBazy'),
]