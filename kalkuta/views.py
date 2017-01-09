from django.contrib.auth.decorators import login_required
import logging
stdlogger = logging.getLogger(__name__)

from .forms import *
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *
from django.utils import timezone


LOG_FILENAME = 'example.log'
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)

MONTH_CHOICES = {1:"Januar", 2:"Februar", 3:"Marec", 4:"April", 5:"Maj", 6:"Junij",
                 7:"Julij", 8:"Avgust", 9:"September", 10:"Oktober", 11:"November", 12:"December"}

mesec_danes = timezone.now().month
leto_danes = timezone.now().year

mesec_danes_fix = timezone.now().month
leto_danes_fix = timezone.now().year

pologi_ta_mesec = 0
stroski_ta_mesec = 0

def racunaj_ta_mesec(request):
    current_user = request.user
    global stroski_ta_mesec
    global pologi_ta_mesec

    vse_trans = Transakcija.objects.filter(uporabnik=current_user).filter(leto_trans=leto_danes).filter(
        mesec_trans=mesec_danes).order_by('-id')

    vse_trans_polog = [0]*31
    vse_trans_strosek = [0]*31

    for i in vse_trans:
        if i.tip == 0:
            vse_trans_strosek[int(i.datum.date().day)] += i.visina
        else:
            vse_trans_polog[int(i.datum.date().day)] += i.visina

    stdlogger.debug(vse_trans_polog)
    stdlogger.debug(vse_trans_strosek)

    stroski_ta_mesec = 0
    pologi_ta_mesec = 0

    for i in vse_trans_polog:
        pologi_ta_mesec += i

    for i in vse_trans_strosek:
        stroski_ta_mesec += i
    return


"""Landing page view"""
def landing(request):
    return render(request, 'kalkuta/index.html')


def izracunaj_leto(request):

    global mesec_danes
    global leto_danes


    stdlogger.debug("Racunam leto")
    if request.method == 'GET':
        nz = request.GET.get('q', '')
        if nz == '1':
            if mesec_danes == 12:
                mesec_danes = 1
                leto_danes += 1
            else:
                mesec_danes += 1
            stdlogger.debug("===============================")
            stdlogger.debug("Pristejem 1 mesec, dobim mesec:")
            stdlogger.debug(mesec_danes)
            stdlogger.debug("in leto:")
            stdlogger.debug( leto_danes)
            stdlogger.debug("===============================")
        elif nz == '-1':
            if mesec_danes == 1:
                mesec_danes = 12
                leto_danes -= 1
            else:
                mesec_danes -= 1
            stdlogger.debug("===============================")
            stdlogger.debug("Odstejem 1 mesec, dobim mesec:")
            stdlogger.debug(mesec_danes)
            stdlogger.debug("in leto:")
            stdlogger.debug( leto_danes)
            stdlogger.debug("===============================")
    return

"""Dashboard view"""
@login_required
def dash(request):
    stdlogger.debug("Entering dash view")
    izracunaj_leto(request)
    racunaj_ta_mesec(request)
    global MONTH_CHOICES

    current_user = request.user
    if not Stanje.objects.filter(uporabnik=current_user):
        stanje = Stanje(stanje=0, uporabnik=current_user)
        stanje.save()

    zadnje_tri = Transakcija.objects.filter(uporabnik=current_user).filter(leto_trans=leto_danes).filter(mesec_trans=mesec_danes).order_by('-id')[:5][::-1]
    zadnje_tri = reversed(zadnje_tri)

    vse_trans = Transakcija.objects.filter(uporabnik=current_user).filter(leto_trans=leto_danes).filter(
        mesec_trans=mesec_danes).order_by('-id')

    vse_trans_polog = [0]*31
    vse_trans_strosek = [0]*31

    for i in vse_trans:
        if i.tip == 0:
            vse_trans_strosek[int(i.datum.date().day)] += i.visina
        else:
            vse_trans_polog[int(i.datum.date().day)] += i.visina

    stdlogger.debug(vse_trans_polog)
    stdlogger.debug(vse_trans_strosek)

    trenS = Stanje.objects.filter(uporabnik=current_user)[0].stanje

    stroski_ta_mesec = 0
    pologi_ta_mesec = 0

    for i in vse_trans_polog:
        pologi_ta_mesec += i

    for i in vse_trans_strosek:
        stroski_ta_mesec += i


    context_dict = {'transakcije': zadnje_tri,
                    'trenS': trenS,
                    'mesec_danes': MONTH_CHOICES[mesec_danes],
                    'leto_danes': leto_danes,
                    'vse_trans_polog': vse_trans_polog,
                    'vse_trans_strosek': vse_trans_strosek,
                    'stroski':stroski_ta_mesec,
                    'pologi':pologi_ta_mesec}

    return render(request, 'kalkuta/dash.html', context_dict)

"""Prilivi view. """
@login_required
def prilivi(request):
    stdlogger.debug("Entering prilivi view")
    racunaj_ta_mesec(request)
    izracunaj_leto(request)
    global MONTH_CHOICES

    if request.method == 'POST':
        form = DodajPolog(request.POST)
        current_user = request.user
        if form.is_valid():
            polog = Transakcija(tip=1, visina=form.cleaned_data['polog_visina'], datum=timezone.now(), uporabnik=current_user, leto_trans=leto_danes_fix, mesec_trans=mesec_danes_fix)
            polog.save()

            s = Stanje.objects.filter(uporabnik=current_user)[0]
            s.stanje += form.cleaned_data['polog_visina']
            s.save()

    current_user = request.user

    zadnja_dva = Transakcija.objects.filter(uporabnik=current_user).filter(tip=1).filter(leto_trans=leto_danes).filter(mesec_trans=mesec_danes).order_by('-id')[:4][::-1]
    zadnja_dva = reversed(zadnja_dva)
    context_dict = {'pologi': zadnja_dva}

    vsi =  Transakcija.objects.filter(uporabnik=current_user).filter(tip=1).filter(leto_trans=leto_danes).filter(mesec_trans=mesec_danes).order_by('-id')

    trenS = Stanje.objects.filter(uporabnik=current_user)[0].stanje

    context_dict = {'pologi': zadnja_dva,
                     'pologi_vsi': vsi,
                    'trenS': trenS,
                    'mesec_danes': MONTH_CHOICES[mesec_danes],
                    'leto_danes': leto_danes,
                    'stroski': stroski_ta_mesec,
                    'pologi_mesec': pologi_ta_mesec
                    }

    return render(request, 'kalkuta/prilivi.html', context_dict)

"""Odlivi view"""
@login_required
def odlivi(request):
    stdlogger.debug("Entering odlivi view")
    racunaj_ta_mesec(request)
    izracunaj_leto(request)
    global MONTH_CHOICES

    current_user = request.user
    if request.method == 'POST':
        form = DodajStrosek(request.POST)

        if form.is_valid():
            strosek = Transakcija(tip=0, visina=form.cleaned_data['strosek_visina'], datum=timezone.now(), uporabnik=current_user, leto_trans=leto_danes_fix, mesec_trans=mesec_danes_fix)

            s = Stanje.objects.filter(uporabnik=current_user)[0]
            s.stanje -= form.cleaned_data['strosek_visina']
            s.save()
            strosek.save()

    zadnja_dva = Transakcija.objects.filter(uporabnik=current_user).filter(tip=0).filter(leto_trans=leto_danes).filter(mesec_trans=mesec_danes).order_by('-id')[:4][::-1]
    zadnja_dva = reversed(zadnja_dva)
    context_dict = {'stroski': zadnja_dva}

    vsi =  Transakcija.objects.filter(uporabnik=current_user).filter(tip=0).filter(leto_trans=leto_danes).filter(mesec_trans=mesec_danes).order_by('-id')

    trenS = Stanje.objects.filter(uporabnik=current_user)[0].stanje

    context_dict = {'stroski': zadnja_dva,
                     'stroski_vsi': vsi,
                    'trenS': trenS,
                    'mesec_danes': MONTH_CHOICES[mesec_danes],
                    'leto_danes': leto_danes,
                    'stroski_mesec': stroski_ta_mesec,
                    'pologi': pologi_ta_mesec
                    }

    return render(request, 'kalkuta/odlivi.html', context_dict)

"""Cilji view"""
@login_required
def cilji(request):
    stdlogger.debug("Entering cilji view")
    racunaj_ta_mesec(request)
    izracunaj_leto(request)
    global MONTH_CHOICES

    current_user = request.user
    if request.method == 'POST':
        form = DodajCilj(request.POST)

        if form.is_valid():

            tren_stanje = Stanje.objects.filter(uporabnik=current_user)
            if not tren_stanje:
                return render(request, 'kalkuta/dash.html')
            #tren_stanje = tren_stanje.stanje
            visina_cilj = form.cleaned_data['visina_cilja'] + tren_stanje[0].stanje
            rok_datum = form.cleaned_data['rok']
            uspeh = -1
            if timezone.now().date() < rok_datum:
                uspeh = 0
            else:
                uspeh = 2

            cilj = Cilji(ime=form.cleaned_data['ime_cilja'], ciljno_stanje=visina_cilj, rok=rok_datum, uspesnost=uspeh, uporabnik=current_user, leto_trans=leto_danes_fix, mesec_trans=mesec_danes_fix)
            cilj.save()

    nedavni_cilji = Cilji.objects.filter(uporabnik=current_user).filter(leto_trans=leto_danes).filter(mesec_trans=mesec_danes).order_by('-id')[:3][::-1]
    nedavni_cilji = reversed(nedavni_cilji)

    vsi_cilji = Cilji.objects.filter(uporabnik=current_user).filter(leto_trans=leto_danes).filter(mesec_trans=mesec_danes).order_by('-id')

    trenS = Stanje.objects.filter(uporabnik=current_user)[0].stanje

    context_dict = {'cilji': vsi_cilji,
                    'nedavni_cilji': nedavni_cilji,
                    'trenS': trenS,
                    'mesec_danes': MONTH_CHOICES[mesec_danes],
                    'leto_danes': leto_danes,
                    'stroski': stroski_ta_mesec,
                    'pologi': pologi_ta_mesec
                    }

    return render(request, 'kalkuta/cilji.html', context_dict)

"""View za registracijo"""
def register(request):
    stdlogger.debug("Entering register view")

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'],password=form.cleaned_data['password1'],email=form.cleaned_data['email'])
            stanje = Stanje(stanje=0, uporabnik=user)
            stanje.save()

            return HttpResponseRedirect('kalkuta/pregled.html')
    form = RegistrationForm(request.POST)

    return render(request, 'registration/register.html', {'form': form})
