from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from datetime import datetime
from django.utils import timezone

class Transakcija(models.Model):
    tip = models.BooleanField() #0 je strosek 1 je polog
    visina = models.FloatField()
    datum = models.DateTimeField(default=datetime.now)
    uporabnik = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    #   Vrne zadnje tri vnesene transakcije za tega uporabnika.


    def __str__(self):
        return "Transakcija: ", self.tip + " Visina transakcije", self.visina


class Cilji(models.Model):
    ime = models.CharField(max_length=30)
    ciljno_stanje = models.FloatField(default=-2)
    rok = models.DateField(default=datetime.now)
    uspesnost = models.IntegerField(default=-1) #0 je v poteku 1 je uspeh 2 je fail
    uporabnik = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    #   Vrne zadnje tri vnesene transakcije za tega uporabnika.


    def __str__(self):
        return "Cilji: ", self.ime + " Visina cilja", self.ciljno_stanje

    @property
    def je_poteklo(self):
        return datetime.today> self.rok

class Stanje(models.Model):
    stanje = models.FloatField(default=0)
    uporabnik = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)