nova_lista_recepata = []
provjera = False
lista_kategorija = ["dorucak", "predjelo", "glavno jelo", "peciva", "desert"]       #sve kategorije recepata

import random

#trazenje random sifre koja sadrzi tri velika slova abecede i 3 broja
def sifra_recepta():
    brojac = 0
    nasumicna_polja = ""
    slovo = ""
    broj = ""
    while brojac < 3:
        random_slovo = random.randint(65, 90)              #65 == A, 90 == C
        slovo += chr(random_slovo)
        random_broj = random.randint(0, 9)
        broj += str(random_broj)
        nasumicna_polja = slovo + broj
        brojac += 1
    return nasumicna_polja

#upisivanje naziva recepta
def naziv_recepta():
    provjera = True
    while provjera:
        recept = input("Unesite naziv recepta ").lower()
        if recept == "":
            print("Unos nije validan")
        else:
            print(recept)
            provjera = False
    nova_lista_recepata.append(recept)

#upisivanje kategorije recepta
def kategorija_recepta():
    provjera = True
    print("Sve kategorije koje mozete unijeti u digitalnu knjigu recepata su: \
        \n1. Dorucak\n2. Predjelo\n3. Glavno jelo\n4. Peciva\n5. Desert ")
    while provjera:
        kategorija = input("Unesite kategoriju (npr desert) ").lower()
        if kategorija not in lista_kategorija:
            print("Kategorija se ne nalazi u listi kategorija")
        else:
            provjera = False
    nova_lista_recepata.append(kategorija)

#upisivanje sastojaka dok korisnik ne upise kraj
def sastojci_recepta():
    filter = ""     #za provjeru
    sastojci = []
    print("Kada unesete sve potrebne sastojke, molimo vas upisite 'kraj'")
    while filter != "kraj":
        filter = input("Unesite sastojke ").lower()
        if filter != "":
            if filter != "kraj":
                sastojci.append(filter)
        else:
            print("Morate unijeti sastojke")
    nova_lista_recepata.append(sastojci)

#upisivanje koraka pravljenja recepta dok korisnik ne upise kraj  
def koraci_recepta():
    filter = ""     #za provjeru
    koraci = []
    print("Kada unesete sve potrebne korake za pravljenje jela, molimo vas upisite 'kraj'!")
    while filter != "kraj":
        filter = input("Unesite korak za pravljenje jela ").lower()
        if filter != "":
            if filter != "kraj":
                koraci.append(filter)
        else:
            print("Morate unijeti korake")
    nova_lista_recepata.append(koraci)

from recepti.pretraga_recepata import pretraga_recepta, ocjenjivanje_recepta
from recepti.brisanje_recepata import brisanje_recepta
from recepti.prikaz_recepta import prikazivanje_recepta
#ovde se nalazi korisnicki meni odnosno u sta sve prijavljeni korisnik moze da udje
def korisnicki_meni(korisnicko_ime):
    provjera = True
    print("---DOBRODOSLI U MENI KORISNIKA---")
    print("Upisite broj ispred stavke ukoliko zelite da otvorite odredjenu stavku \
        \n1. Dodavanje recepta\n2. Pretraga recepta\n3. Ocenjivanje recepta\n4. Brisanje recepta\n5. Prikaz i stampanje recepta")
    while provjera:
        try:
            unos = int(input("Unesite broj ispred stavke bez tacke "))
            if unos == 1:
                provjera = False
                return dodavanje_recepta(korisnicko_ime)
            elif unos == 2:
                provjera = False
                return pretraga_recepta()
            elif unos == 3:
                provjera = False
                return ocjenjivanje_recepta(korisnicko_ime)
            elif unos == 4:
                provjera = False
                return brisanje_recepta(korisnicko_ime)
            elif unos == 5:
                provjera = False
                return prikazivanje_recepta()
            else:
                print("Pogresan unos")
        except ValueError:
            print("Molimo vas da uneste jedan broj od 1 do 5")


import json
rjecnik = {}
#dodavanje recepta u recepti.json
def dodavanje_recepta(korisnicko_ime):
    print("---DODAVANJE RECEPTA---")
    lista_recepata = []
    sifra = ""
    with open("data/recepti.json", "r", encoding="utf-8") as fp:
        lista_recepata = json.load(fp)
    while sifra in lista_recepata:
        sifra_recepta()
    sifra = sifra_recepta()
    nova_lista_recepata.append(sifra)
    nova_lista_recepata.append(korisnicko_ime)
    naziv_recepta()
    kategorija_recepta()
    sastojci_recepta()
    koraci_recepta()
    print(nova_lista_recepata)
    rjecnik = {
        "sifra" : nova_lista_recepata[0],
        "korisnik" : nova_lista_recepata[1],
        "naziv" : nova_lista_recepata[2],
        "kategorija" : nova_lista_recepata[3],
        "sastojci" : nova_lista_recepata[4],
        "koraci" : nova_lista_recepata[5]
    }  
    lista_recepata.append(rjecnik)
    with open("data/recepti.json", "w") as fajl:
        json.dump(lista_recepata , fajl, indent=4)




