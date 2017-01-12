from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
import logging
stdlogger = logging.getLogger(__name__)

from datetime import datetime


"""Tabela transakcija, ki spremlja transakcije - stroske ter pologe."""
class Transakcija(models.Model):
    tip = models.BooleanField() #0 je strosek 1 je polog
    visina = models.FloatField()
    datum = models.DateTimeField(default=datetime.now)
    uporabnik = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    leto_trans = models.IntegerField(null=True)
    mesec_trans = models.IntegerField(null=True)

    def __str__(self):
        return "Transakcija: ", self.tip + " Visina transakcije", self.visina


"""Tabela cilji, ki spremlja cilje."""
class Cilji(models.Model):
    ime = models.CharField(max_length=30)
    ciljno_stanje = models.FloatField(default=-2)
    rok = models.DateField(default=datetime.now)
    uspesnost = models.IntegerField(default=-1) #0 je v poteku 1 je uspeh 2 je fail
    uporabnik = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    leto_trans = models.IntegerField(null=True)
    mesec_trans = models.IntegerField(null=True)


    def __str__(self):
        return "Cilji: ", self.ime + " Visina cilja", self.ciljno_stanje

    @property
    def je_poteklo(self):
        return datetime.today> self.rok


"""Tabela stanja na racunu.  Vsak racun ima enega uporabnika in en uporabnik ima en racun."""
class Stanje(models.Model):
    stanje = models.FloatField(default=0)
    uporabnik = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
