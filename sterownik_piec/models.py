from django.db import models

class Czujniki(models.Model):
    nazwa = models.CharField(max_length=20)
    wartosc = models.FloatField()
    typ = models.CharField(max_length=1)

    def set(self):
        pass

    def get(self):
        pass