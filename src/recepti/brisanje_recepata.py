lista_recepata = []
lista_ocjena = []
rjecnik_recepata = {}
lista_recepata_jednog_korisnika = []
import json
def brisanje_recepta(korisnicko_ime):
    print("---BRISANJE RECEPATA---")
    with open("data/recepti.json", "r", encoding="utf-8") as fajl:
        lista_recepata = json.load(fajl)
    print(lista_recepata)
    with open("data/ocene.json", "r", encoding="utf-8") as fajl2:
        lista_ocjena = json.load(fajl2)
    print(lista_ocjena)
    redni_broj = 0
    brojac = 0          #za brojanje ocjena
    prosjecna_ocjena = 0
    suma = 0
    for red in lista_recepata:
        if korisnicko_ime == red["korisnik"]:
            redni_broj = redni_broj + 1
            rjecnik_recepata["redni broj"] = redni_broj
            rjecnik_recepata["sifra"] = red["sifra"]
            rjecnik_recepata["naziv"] = red["naziv"]
            for linija in lista_ocjena:
                if linija["sifra"] == red["sifra"]:
                    brojac = brojac + 1
                    suma = suma + linija["ocena"]
                    prosjecna_ocjena = suma / brojac
                    rjecnik_recepata["prosjecna ocjena"] = prosjecna_ocjena
            lista_recepata_jednog_korisnika.append(rjecnik_recepata)
    print(lista_recepata_jednog_korisnika)
    provjera = True
    while provjera:
        unos = str(input("Unesite sifru recepta koji zelite da obrisete ")).upper()
        for red in lista_recepata:
            if unos == red["sifra"]:
                if korisnicko_ime == red["korisnik"]:
                    print(red)
                    lista_recepata.remove(red)
                    break
                else:
                    print("Ne mozete da brisete recept koji nije vas. Prijatno")
                    return
        for red in lista_ocjena:
            if unos == red["sifra"]:
                lista_ocjena.remove(red)
        provjera = False       
    with open("data/recepti.json", "w", encoding="utf-8") as fp:
        json.dump(lista_recepata, fp, indent=4)
    with open("data/ocene.json", "w", encoding="utf-8") as fp:
        json.dump(lista_ocjena, fp, indent=4)
    print("Recept je uspjesno obrisan")

    
        



        
    
