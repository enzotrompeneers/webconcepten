from __future__ import unicode_literals
from django.db import models

class Klassen(models.Model):
    naam = models.CharField(max_length=100)
    numeriekeCode = models.CharField(max_length=100)
    richting = models.CharField(max_length=100)
    leeraar = models.CharField(max_length=255)
    def __str__(self):
        return '%s %s %s %s' % (self.naam, self.numeriekeCode, self.richting, self.leeraar)

class Richtingen(models.Model):
    klassen = models.ForeignKey(Klassen, on_delete=models.CASCADE)
    naam = models.CharField(max_length=100)
    omschrijving = models.CharField(max_length=255)
    def __str__(self):
        return '%s %s' % (self.naam, self.omschrijving)

class Leraren(models.Model):
    klassen = models.ForeignKey(Klassen, on_delete=models.CASCADE)
    naam = models.CharField(max_length=100)
    voornaam = models.CharField(max_length=100)
    foto = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    def __str__(self):
        return '%s %s %s %s' % (self.naam, self.voornaam, self.foto, self.email)
        
class Contact(models.Model):
    email = models.CharField(max_length=255)
    telefoonNr = models.CharField(max_length=100)
    adres = models.CharField(max_length=255)
    bericht = models.CharField(max_length=255)
    def __str__(self):
        return '%s %s %s %s' % (self.email, self.telefoonNr, self.adres, self.bericht)