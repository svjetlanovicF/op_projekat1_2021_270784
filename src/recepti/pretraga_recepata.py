provjera = False

# u ovoj funkciji se bira hoce li se vrsiti pretraga na osnovu kategorije ili naziva
def pretraga_recepta():
    provjera = True
    print("---PRETRAGA RECEPTA---")
    print("Pretraga recepta se vrsi na dva nacina tj. na osnovu naziva recepta ili kategorije recepta")
    while provjera:
        unos = input("Unesite pojam 'naziv' ili 'kategorija' ").lower()
        if unos == "naziv":        
            return pretraga_po_nazivu()
        elif unos == "kategorija":
            return pretraga_po_kategoriji()
        else:
            print("Unos nije validan. Unesite ponovo!")

#ova funkcija pretrazuje da li je unijeti naziv u jednom od recepata, ako jeste, salje ga u prikaz_po_pretrazi_recepta
def pretraga_po_nazivu():
    provjera = True
    with open("data/recepti.json", "r", encoding="utf-8") as fajl:
        lista_dodavanih_recepata = json.load(fajl)
    print(lista_dodavanih_recepata)
    while provjera:
        naziv = str(input("Unesite naziv jela ")).lower()
        for red in lista_dodavanih_recepata:
            if naziv in red["naziv"]:
                if len(naziv) >= 3:           #ukoliko ima tri ili vise karaktera
                    prikaz_po_pretrazi_recepta(broj = 2, ime_recepta = naziv)
                    provjera = False
                    break


from meni.meni_korisnika import lista_kategorija
#vrsi se pretraga po kategoriji odnosno korisnik unosi koju kategoriju zeli i salje se metodi prikaz_po_pretrazi_recepta
def pretraga_po_kategoriji():
    provjera = True 
    print("Sve kategorije koje mozete unijeti u digitalnu knjigu recepata su: \
        \n1. Dorucak\n2. Predjelo\n3. Glavno jelo\n4. Peciva\n5. Desert ")
    while provjera:
        try:
            unos = int(input("Unesite kategoriju (npr 1) "))
            if unos == 1:
                return prikaz_po_pretrazi_recepta( broj = 1, kategorija = lista_kategorija[0])
            elif unos == 2:
                return prikaz_po_pretrazi_recepta(broj = 1, kategorija = lista_kategorija[1])
            elif unos == 3:
                return prikaz_po_pretrazi_recepta( broj = 1, kategorija = lista_kategorija[2])
            elif unos == 4:
                return prikaz_po_pretrazi_recepta(broj = 1, kategorija = lista_kategorija[3])
            elif unos == 5:
                return prikaz_po_pretrazi_recepta( broj = 1, kategorija = lista_kategorija[4])
            else:
                print("Ne nalazi se u list kategorija")
        except ValueError:
            print("Unos nije validan")


import json
lista_prikaza = []
lista_korisnika = []
#ova metoda izlistava recept na osnovu kategorije ako je broj 1 i ako je preko naziva trazio recept broj 2
def prikaz_po_pretrazi_recepta(broj,  kategorija = "", ime_recepta = ""):
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
    lista_dodavanih_recepata = []
    lista_ocjena = []
    with open("data/recepti.json", "r", encoding="utf-8") as fajl:
        lista_dodavanih_recepata = json.load(fajl)
    with open("data/ocene.json", "r", encoding="utf-8") as fajl2:
        lista_ocjena = json.load(fajl2)
    brojac = 0
    i = 0
    redni_broj = 0
    rjecnik_prikaza = {}
    if broj == 1:
        for red in lista_dodavanih_recepata: 
            if kategorija == red["kategorija"]:
                # redni_broj = redni_broj + 1
                rjecnik_prikaza["redni broj"] = redni_broj +1
                rjecnik_prikaza["sifra"] = red["sifra"]
                rjecnik_prikaza["naziv"] = red["naziv"]
                for rjecnik in lista_korisnika:
                    if red["korisnik"] == rjecnik["korisnicko ime"]:
                        rjecnik_prikaza["ime i prezime"] = rjecnik["ime"] + " " + rjecnik["prezime"]
                        for linija in lista_ocjena:
                            if red["sifra"] == linija["sifra"]:
                                i = i + 1
                                brojac = brojac + linija["ocena"]
                                if(i != 0):
                                    rjecnik_prikaza["prosjecna ocjena"] = brojac / i
                        lista_prikaza.append(rjecnik_prikaza)
        print(lista_prikaza)
        return lista_prikaza
                    
    elif broj == 2:
        for red in lista_dodavanih_recepata:
            if ime_recepta in red["naziv"]:
                redni_broj = redni_broj + 1
                rjecnik_prikaza["redni broj"] = redni_broj
                rjecnik_prikaza["sifra"] = red["sifra"]
                rjecnik_prikaza["naziv"] = red["naziv"]
                for rjecnik in lista_korisnika:
                    if red["korisnik"] == rjecnik["korisnicko ime"]:
                        rjecnik_prikaza["ime i prezime"] = rjecnik["ime"] + " " + rjecnik["prezime"]
                        for linija in lista_ocjena:
                            if red["sifra"] == linija["sifra"]:
                                i = i + 1
                                brojac = brojac + linija["ocena"]
                                if(i != 0):
                                    rjecnik_prikaza["prosjecna ocjena"] = brojac / i
                        lista_prikaza.append(rjecnik_prikaza)
        print(lista_prikaza)
        return lista_prikaza     

#vrsi se pretraga recepta na osnovu unosa korisnika i poziva se metoda upisivanje_ocjena       
def ocjenjivanje_recepta(korisnicko_ime):
    pretraga_recepta()
    trenutna_lista = []
    trenutni_rjecnik = {}
    provjera = True
    while provjera:
        try:
            unos = int(input("Unesite redni broj recepta "))
            for red in lista_prikaza:
                if unos == red["redni broj"]:
                    trenutni_rjecnik = {
                        "redni broj" : red["redni broj"],
                        "sifra" : red["sifra"],
                        "naziv" : red["naziv"],
                        "ime i prezime" : red["ime i prezime"]
                    }
                trenutna_lista.append(trenutni_rjecnik)
            provjera = False
            return upisivanje_ocjena(trenutna_lista, korisnicko_ime)
        except ValueError:
            print("Pogresan unos")


#vrsi se upisivanje ocjene u ocene.json
def upisivanje_ocjena(recept, korisnicko_ime):
    for red in recept:
        print(red)
    lista_ocjena = []
    privremeni_rjecnik = {}
    provjera = True
    with open("data/ocene.json", "r", encoding="utf-8") as fajl:
        lista_ocjena = json.load(fajl)
    sifra = recept[0]["sifra"]              
    for red in lista_ocjena:
        if sifra == red["sifra"]:
            while provjera:
                try:
                    unos = int(input("Unesite ocjenu od 1-5 brojevima "))
                    if unos == 1 or unos == 2 or unos == 3 or unos == 4 or unos == 5:
                        privremeni_rjecnik["sifra"] = red["sifra"]
                        privremeni_rjecnik["korisnik"] = korisnicko_ime
                        privremeni_rjecnik["ocena"] = unos
                except ValueError:
                    print("Nevalidan unos")
                komentar = str(input("Ako zelite, napisite svoje misljenje o receptu "))
                privremeni_rjecnik["komentar"] = komentar
                provjera = False
            lista_ocjena.append(privremeni_rjecnik)
            break
        else:
            while provjera:
                try:
                    unos = int(input("Unesite ocjenu od 1-5 brojevima "))
                    if unos == 1 or unos == 2 or unos == 3 or unos == 4 or unos == 5:
                        privremeni_rjecnik["sifra"] = red["sifra"]
                        privremeni_rjecnik["korisnik"] = korisnicko_ime
                        privremeni_rjecnik["ocena"] = unos
                except ValueError:
                    print("Nevalidan unos")
                komentar = str(input("Ako zelite, napisite svoje misljenje o receptu "))
                privremeni_rjecnik["komentar"] = komentar
                provjera = False
            lista_ocjena.append(privremeni_rjecnik)
            break
    with open("data/ocene.json", "w", encoding="utf-8") as fajl:
        json.dump(lista_ocjena, fajl, indent=4)
    brojac = 0
    i = 0           #sabira ocjene
    prosjecna_ocjena = 0
    svi_komentari = ""
    for red in lista_ocjena:
        if red["sifra"] == recept[0]["sifra"]:
            svi_komentari = str(svi_komentari + "\n" + red["komentar"])
            brojac = brojac + 1
            i = i + red["ocena"]
            prosjecna_ocjena = i / brojac
        else:
            svi_komentari = str(svi_komentari + "\n" + red["komentar"])
            brojac = brojac + 1
            i = i + red["ocena"]
            prosjecna_ocjena = i / brojac
    print(svi_komentari)
    print("Prosjecna ocjena", prosjecna_ocjena)


    


    
    
