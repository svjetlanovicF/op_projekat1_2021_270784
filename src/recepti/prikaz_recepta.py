provjera = False
from recepti.pretraga_recepata import pretraga_recepta

def prikazivanje_recepta():
    print("---PRIKAZIVANJE I STAMPANJE RECEPTA---")
    print("Prikaz recepta mozete ostvariti tako sto cete unijeti sifru zeljenog recepta ili pomocu pretrage recepta")
    provjera = True
    while provjera:
        try:
            print("Unesite broj 1 ako zelite da vrsite pretragu pomocu sifre ili broj 2 ako cete vrsiti pomocu kategorije ili naziva ")
            unos = int(input())
            if unos == 1:
                provjera = False
                return prikazivanje_recepta_pomocu_sifre()
            elif unos == 2:
                provjera = False
                return prikazivanje_recepta_pomocu_pretrage()
            else:
                print("Unos nije validan!")   
        except ValueError:
            print("Unos nije validan!")

lista_recepata = []
lista_ocjena = []
import json
from recepti.pretraga_recepata import lista_korisnika
def prikazivanje_recepta_pomocu_sifre():
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
    uslov = True
    prosjecna_ocjena = 0
    brojac = 0
    suma = 0
    komentari = ""
    privremena_lista = []
    ime_prezime = ""
    ime_komentar = ""
    with open("data/recepti.json", "r", encoding="utf-8") as fajl:
        lista_recepata = json.load(fajl)
    with open("data/ocene.json", "r", encoding="utf-8") as fp:
        lista_ocjena = json.load(fp)
    print(lista_korisnika)
    while uslov:
        unos = str(input("Unesite sifru ")).upper()
        if unos != "":
            for red in lista_recepata:
                if unos == red["sifra"]:
                    privremena_lista.append(red)
                    for linija in lista_ocjena:
                        if unos == linija["sifra"]:
                            brojac = brojac + 1
                            suma = suma + int(linija["ocena"])
                            prosjecna_ocjena = suma / brojac
                            for imena in lista_korisnika:
                                if linija["korisnik"] == imena["korisnicko ime"]:
                                    ime_prezime = imena["ime"] + " " + imena["prezime"] + " - "
                                    komentari = linija["komentar"] + "."
                                    ime_komentar += ime_prezime + komentari
                                    
            uslov = False
        else:
            print("Ponovite unos")
    privremena_lista.append(ime_komentar)
    privremena_lista.append(prosjecna_ocjena)
    naziv_datoteke = ""
    naziv_datoteke ="data/tekstualne_datoteke/" + privremena_lista[0]["sifra"] + "-" + privremena_lista[0]["naziv"] + ".txt"
    stampanje_teksta = ""
    stampanje_teksta = str(privremena_lista[0]["sifra"]) + "\n" +  str(privremena_lista[0]["korisnik"]) + "\n" \
+ str(privremena_lista[0]["naziv"]) + "\n" + str(privremena_lista[0]["kategorija"]) + "\n" + str(privremena_lista[0]["sastojci"])  \
    + "\n" +  str(privremena_lista[0]["koraci"]) + "\n" + str(privremena_lista[1]) + "\n" + str(privremena_lista[2])
    with open(naziv_datoteke, "w", encoding="utf-8") as fp:
        fp.writelines(stampanje_teksta)
    print(privremena_lista)
    print("Recept je istampan u datoteku.")
    
def prikazivanje_recepta_pomocu_pretrage():   

    ime_komentar = ""
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
    privremena_lista_ocjena = []
    privremena_lista_recepata = []
    komentari = ""
    with open("data/ocene.json", "r", encoding="utf-8") as fp:
        privremena_lista_ocjena = json.load(fp)
    with open("data/recepti.json", "r", encoding="utf-8") as fp2:
        privremena_lista_recepata = json.load(fp2)
    lista_pretrage = pretraga_recepta()
    for red in lista_pretrage:
        for linija in privremena_lista_ocjena:
            if red["sifra"] == linija["sifra"]:
                for imena in lista_korisnika:
                    if linija["korisnik"] == imena["korisnicko ime"]:
                        ime_prezime = imena["ime"] + " " + imena["prezime"] + " - "
                        komentari = linija["komentar"] + ". "
                        ime_komentar += ime_prezime + komentari
    
    naziv_datoteke = ""
    stampanje_teksta = ""
    for red in lista_pretrage:
        for linija in privremena_lista_recepata:
            if linija["sifra"] == red["sifra"]:
                stampanje_teksta = stampanje_teksta = str(linija["sifra"]) + "\n" +  str(linija["korisnik"]) + "\n" \
+ str(linija["naziv"]) + "\n" + str(linija["kategorija"]) + "\n" + str(linija["sastojci"])  \
    + "\n" +  str(linija["koraci"]) + "\n" + ime_komentar
    naziv_datoteke = "data/tekstualne_datoteke/" + lista_pretrage[0]["sifra"] + "-" + lista_pretrage[0]["naziv"] + ".txt"
    with open(naziv_datoteke, "w", encoding="utf-8") as fp:
        fp.writelines(stampanje_teksta)
    print(stampanje_teksta)
    print("Recept je istampan u datoteku.")
