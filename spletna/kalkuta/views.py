from django.contrib.auth.decorators import login_required
from docutils.nodes import tip

from .forms import *
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *
from django.utils import timezone

def landing(request):
    return render(request, 'kalkuta/index.html')

@login_required
def dash(request):
    current_user = request.user
    if not Stanje.objects.filter(uporabnik=current_user):
        stanje = Stanje(stanje=0, uporabnik=current_user)
        stanje.save()

    zadnje_tri = Transakcija.objects.filter(uporabnik=current_user).order_by('-id')[:5][::-1]
    zadnje_tri = reversed(zadnje_tri)


    trenS = Stanje.objects.filter(uporabnik=current_user)[0].stanje
    context_dict = {'transakcije': zadnje_tri,
                    'trenS': trenS}
    return render(request, 'kalkuta/dash.html', context_dict)

@login_required
def prilivi(request):
    if request.method == 'POST':
        form = DodajPolog(request.POST)
        current_user = request.user
        if form.is_valid():
            polog = Transakcija(tip=1, visina=form.cleaned_data['polog_visina'], datum=timezone.now(), uporabnik=current_user)
            polog.save()

            s = Stanje.objects.filter(uporabnik=current_user)[0]
            s.stanje += form.cleaned_data['polog_visina']
            s.save()

    current_user = request.user

    zadnja_dva = Transakcija.objects.filter(uporabnik=current_user).filter(tip=1).order_by('-id')[:4][::-1]
    zadnja_dva = reversed(zadnja_dva)
    context_dict = {'pologi': zadnja_dva}

    vsi =  Transakcija.objects.filter(uporabnik=current_user).filter(tip=1).order_by('-id')

    trenS = Stanje.objects.filter(uporabnik=current_user)[0].stanje

    context_dict = {'pologi': zadnja_dva,
                     'pologi_vsi': vsi,
                    'trenS': trenS}

    return render(request, 'kalkuta/prilivi.html', context_dict)


@login_required
def odlivi(request):
    current_user = request.user
    if request.method == 'POST':
        form = DodajStrosek(request.POST)

        if form.is_valid():
            strosek = Transakcija(tip=0, visina=form.cleaned_data['strosek_visina'], datum=timezone.now(), uporabnik=current_user)

            s = Stanje.objects.filter(uporabnik=current_user)[0]
            s.stanje -= form.cleaned_data['strosek_visina']
            s.save()
            strosek.save()

    zadnja_dva = Transakcija.objects.filter(uporabnik=current_user).filter(tip=0).order_by('-id')[:4][::-1]
    zadnja_dva = reversed(zadnja_dva)
    context_dict = {'stroski': zadnja_dva}

    vsi =  Transakcija.objects.filter(uporabnik=current_user).filter(tip=0).order_by('-id')

    trenS = Stanje.objects.filter(uporabnik=current_user)[0].stanje

    context_dict = {'stroski': zadnja_dva,
                     'stroski_vsi': vsi,
                    'trenS': trenS}

    return render(request, 'kalkuta/odlivi.html', context_dict)

@login_required
def cilji(request):
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

            cilj = Cilji(ime=form.cleaned_data['ime_cilja'], ciljno_stanje=visina_cilj, rok=rok_datum, uspesnost=uspeh, uporabnik=current_user)
            cilj.save()

    nedavni_cilji = Cilji.objects.filter(uporabnik=current_user).order_by('-id')[:3][::-1]
    nedavni_cilji = reversed(nedavni_cilji)

    vsi_cilji = Cilji.objects.filter(uporabnik=current_user).order_by('-id')

    trenS = Stanje.objects.filter(uporabnik=current_user)[0].stanje

    context_dict = {'cilji': vsi_cilji,
                    'nedavni_cilji': nedavni_cilji,
                    'trenS': trenS}

    return render(request, 'kalkuta/cilji.html', context_dict)


def register(request):
    args = {}
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'],password=form.cleaned_data['password1'],email=form.cleaned_data['email'])
            stanje = Stanje(stanje=0, uporabnik=user)
            stanje.save()

            return HttpResponseRedirect('kalkuta/pregled.html')
    form = RegistrationForm(request.POST)

    return render(request, 'registration/register.html', {'form': form})
