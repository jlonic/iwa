from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Projekcija(models.Model):
    ime_filma=models.CharField(max_length=100)
    vrijeme_filma=models.IntegerField()
    kapacitet=models.IntegerField()
    
    def broj_slobodnih_mjesta(self):
        return self.kapacitet-self.karta_set.count() #foreign key
    

class Karta(models.Model):
    broj_sjedala=models.IntegerField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    projekcija=models.ForeignKey(Projekcija, on_delete=models.CASCADE)

    def dodijeli_broj_sjedala(self):
        zauzeta_sjedala=Karta.objects.filter(projekcija=self.projekcija).count() #broji karte za odredenu projekciju
        if (zauzeta_sjedala<self.projekcija.kapacitet): #manje karata od kapaciteta = +1 za novu kartu
            self.broj_sjedala=zauzeta_sjedala+1
