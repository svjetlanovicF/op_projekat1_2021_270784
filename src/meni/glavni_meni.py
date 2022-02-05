#glavni meni aplikacije se sastoji od registracije, prijave i izlaska iz aplikacije
lista_korisnika = []        #podaci za registraciju
lista_prijava = []          #podaci za prijavu
nova_lista_korisnika = []  
provjera = False
prijavljeni_korisnici = []
korisnicko_ime = ""

with open("data/korisnici.csv", encoding="utf-8") as fp:
    for red in fp:
        vrijednosti = red.strip().split(",")
        registrovani_korisnici = {
            "ime" : vrijednosti[0],
            "prezime" : vrijednosti[1],
            "korisnicko ime" : vrijednosti[2],
            "sifra" : vrijednosti[3],
            "email" : vrijednosti[4]
        }
        lista_korisnika.append(registrovani_korisnici)
        lista_prijava = [lista for element in lista_korisnika
                        for lista in element.values()]          #cuvanje svih vrijednosti kao lista
    print(lista_korisnika)

def meni():
    print("---DOBRODOSLI U DIGITALNU KNJIGU RECEPATA.---\nGLAVNI MENI APLIKACIJE\
(unesite broj koji se nalazi ispred stavke):\n1. Prijava\n2. Registracija\n3. Izlazak iz aplikacije")
    provjera = True
    while provjera:
        try:
            unos = int(input("Unesite broj bez tačke "))
            if unos == 1:
                provjera = False
                print("---PRIJAVA---")
                return prijava()
            if unos == 2:
                print("---REGISTRACIJA---")
                provjera = False
                return registracija_korisnika()     #ubaciti return ako baguje
            if unos == 3:
                exit()
            else:
                print("Pogrešan unos. Molim Vas ponovite svoj unos")
        except ValueError:
            print("Pogrešan unos. Molim Vas ponovite svoj unos")


#uzimanje imena korisnika
def ime_korisnika():
    provjera = True
    while provjera:
        ime = str(input("Unesite Vase ime ")).lower()
        if ime != "":
            nova_lista_korisnika.append(ime)
            provjera = False
        else:
            print("Pogresan unos")

#uzimanje prezimena korisnika
def prezime_korisnika():
    provjera = True
    while provjera:
        prezime = str(input("Unesite Vase prezime ")).lower()
        if prezime != "":
            nova_lista_korisnika.append(prezime)
            provjera = False
        else:
            print("Pogresan unos")

#uzimanje korisnickog imena korisnika
def korisnicko_ime_korisnika():
    provjera = True
    while provjera:
        korisnicko_ime = str(input("Unesite korisnicko ime ")).lower()
        if korisnicko_ime != "":
            if korisnicko_ime not in lista_prijava:
                provjera = False
                nova_lista_korisnika.append(korisnicko_ime)
            else:
                print("Korisnicko ime vec postoji.")
        else:
            print("Pogresan unos.")

#uzimanje sifre korisnika
def sifra_korisnika():
    provjera = True
    while provjera:
        sifra = str(input("Sifra Mora da sadrzi najmanje 6 karaktera. Unesite sifru ")).lower()
        if len(sifra) < 6:
            print("Sifra ne smije da sadrzi manje od 6 karaktera")
        else:
            provjera = False
            nova_lista_korisnika.append(sifra)

"""
email - ^ i $ pocetak i kraj stringa
prve []+ znace da moze da sadrzi slova i brojeve jednom ili vise puta
[\.]? - moze da sadrzi jednom ili nijednom
\w mora da sadrzi a-zA-Z0-9 jedan ili vise
\w{2,3} mora sadrzati od 2 do 3 karaktera
"""

import re
def email_korisnika():
    provjera = True
    izraz = "^[a-zA-Z0-9]+[\._]?[a-zA-Z0-9]+[@]\w+[.]\w{2,3}$"      
    while provjera:
        email = str(input("Unesite email "))
        if email != "":
            if(re.search(izraz, email)):
                if email not in lista_prijava:
                    nova_lista_korisnika.append(email + "\n")      #dodaj + "\n" ako ne radi
                    provjera = False
                else:
                    print("Email vec postoji")
            else:
                print("Pogresan unos")   
        else:
            print("Pogresan unos")

def registracija_korisnika():
    ime_korisnika()
    prezime_korisnika()
    korisnicko_ime_korisnika()
    sifra_korisnika()
    email_korisnika()
    with open("data/korisnici.csv", "a", encoding="utf-8") as fajl:
        fajl.write(",".join(nova_lista_korisnika))
    provjera = True
    print("Uspjesno ste registrovani." + "\n" +  "Ukoliko zelite da se prijavite upisite broj 1 a ukoliko zelite da izadjete pritisnite broj 2")
    while provjera:
        try:
            prijava_korisnika = int(input("Unesite broj "))
            if prijava_korisnika == 1:
                provjera = False
                return prijava()
            elif prijava_korisnika == 2:
                provjera = False
                exit()
            else:
                print("Pogresan unos")
        except ValueError:
            print("Pogresan unos")


def korisnicko_ime_za_prijavu():
    provjera = True
    while provjera:
        korisnicko_ime = str(input("Unesite korisnicko ime za prijavu ")).lower()
        for red in lista_korisnika:
            if korisnicko_ime != "":
                if korisnicko_ime == red["korisnicko ime"]:
                    provjera = False
                    return korisnicko_ime
        print("Korisnicko ime ne postoji")

                

def sifra_za_prijavu(korisnicko_ime):
    provjera = True
    while provjera:
        sifra = str(input("Unesite sifru za prijavu ")).lower()
        for red in lista_korisnika:
            if sifra == red["sifra"]:
                if korisnicko_ime == red["korisnicko ime"]:             #provjeravanje da li se u tom redu nalazi korisnicko ime cija je sifra
                    print("USPJESNO STE PRIJAVLJENI " + red["ime"].upper() + "!")
                    prijavljeni_korisnici.append(korisnicko_ime)
                    prijavljeni_korisnici.append(sifra)
                    provjera = False
                    return sifra
        print("Sifra ne postoji!")

from meni.meni_korisnika import korisnicki_meni
def prijava():
    with open("data/korisnici.csv", encoding="utf-8") as fp:
        for red in fp:
            vrijednosti = red.strip().split(",")
            registrovani_korisnici = {
                "ime" : vrijednosti[0],
                "prezime" : vrijednosti[1],
                "korisnicko ime" : vrijednosti[2],
                "sifra" : vrijednosti[3],
                "email" : vrijednosti[4]
            }
            lista_korisnika.append(registrovani_korisnici)    
    korisnicko_ime = korisnicko_ime_za_prijavu()
    sifra_za_prijavu(korisnicko_ime)
    korisnicki_meni(korisnicko_ime)
