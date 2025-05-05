from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Evenement, Participation
from django.contrib.auth.forms import AuthenticationForm
from .forms import ConnexionForm



# connexion-------------


def connexion(request):
    if request.user.is_authenticated:
        return redirect('listeEvent')

    form = ConnexionForm()
    if request.method == 'POST':
        form = ConnexionForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('listeEvent')  
    return render(request, 'connexion.html', {'formulaire': form})

# listEvent-------------

def listeEvent(request):
    evenements = Evenement.objects.all()
    for evenement in evenements:
        evenement.nombre_participants = Participation.objects.filter(evenement=evenement).count()
    return render(request, 'listeEvent.html', {'evenements': evenements})


# detailevent-------------


def detailevent(request, event_id):
    evenement = get_object_or_404(Evenement, id=event_id)
    deja_participe = False
    if request.user.is_authenticated:
        deja_participe = Participation.objects.filter(evenement=evenement, utilisateur=request.user).exists()
    nombre_participants = Participation.objects.filter(evenement=evenement).count()
    return render(request, 'detailevent.html', {
        'evenement': evenement,
        'deja_participe': deja_participe,
        'nombre_participants': nombre_participants
    })


# login-------------


@login_required
def participer_evenement(request, event_id):
    evenement = get_object_or_404(Evenement, id=event_id)
    Participation.objects.get_or_create(evenement=evenement, utilisateur=request.user)
    return redirect('detailevent', event_id=event_id)
