from django.shortcuts import render, redirect
from .models import Projekcija, Karta
from django.contrib.auth.models import User
# Create your views here.


def sve_projekcije(request):
    user=User.objects.all() #svi useri
    projekcije=Projekcija.objects.all() #sve projekcije

    if (request.method=="POST"):
        user=User.objects.get(pk=request.POST.get('user')) #dohvaca usera ciji pk=user_id 
        projekcija=Projekcija.objects.get(pk=request.POST.get('projekcija')) #dohvaca film ciji pk=projekcija_id
        #print(user.username)
        #print(projekcija.ime_filma)

        nova_karta=Karta(user=user, projekcija=projekcija) #napravi novu kartu 
        nova_karta.dodijeli_broj_sjedala() 
        nova_karta.save() #sprema u db
        
        return redirect('sve_projekcije') #refresha nakon submita
    return render(request, 'sve_projekcije.html', {'projekcije': projekcije, 'user': user})


def karte_korisnika(request, user_id):
    user=User.objects.get(pk=user_id) #dohvaca usera
    #print(user)
    karte=Karta.objects.filter(user=user) #dohvaca sve karte tog usera
    return render(request, 'karte_korisnika.html', {'user': user, 'karte': karte})