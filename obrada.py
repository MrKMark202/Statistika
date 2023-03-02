import pandas as pd

podaci = pd.read_excel('data.xlsx')

print(podaci) # Prikaz svih podataka
print("\n")

podaci_u_listu = podaci.values.tolist()
#print(podaci_u_listu[][]]) # Debug (provjera selekcije podataka)

natrag: print("Izbornik\n\n1 - Promjena poljoprivredne površine\n2 - Promjena količine goveda\n3 - Predviđanje uroda za trajni nasad za iduću godinu\n4 - Usporedba poljoprivredne površine za 2013. i 2016 godinu")
izbor = int(input("Unesite izbor: "))
print()

if(izbor == 1): # Računanje porasta iskorištene poljoprivredne površine

    print("Porast iskorištene poljoprivredne površine")
    print("----------------------------------------------------------------------------------------------")

    PV = podaci_u_listu[1][1] # Vrijednost poljoprivredne površine u RH tokom 2013. godine
    r = float(input("Unesite željeni postotak (u obliku decimalnog broja od 0 do 1): "))
    n = 3 # Razdoblje 2013.-2016.
    FV = PV * (1 + r) ** n

    # Izračunaj povećanje u odnosu na početnu vrijednost
    porast = FV - PV

    # Izračunaj vjerojatnost povećanja
    vjerojatnost = porast / PV

    # Ispiši rezultate
    print("Buduća vrijednost poljoprivredne površine nakon dvije godine:", FV, "metara kvadratnih")
    print("Povećanje poljoprivredne površine u odnosu na početnu vrijednost:", porast, "metara kvadratnih")
    print("Vjerojatnost povećanja poljoprivredne površine u sljedeće dvije godine:", vjerojatnost)
    print()


elif(izbor == 2): # Predviđanje količine goveda nakon 3 godine

    print("Promjena količine goveda")
    print("----------------------------------------------------------------------------------------------")

    PVgov = podaci_u_listu[1][16] # Broj goveda u RH 2016. godine
    rođeno = float(input("Unesite prosjek rođenog goveda u decimalnom obliku: "))
    uginulo = float(input("Unesite prosjek uginulog goveda u decimalnom obliku: "))

    FVgov1 = PVgov + rođeno - uginulo # Prva godina
    FVgov2 = FVgov1 + rođeno - uginulo # Druga godina
    FVgov3 = FVgov2 + rođeno - uginulo # Treća godina

    print("Broj goveda nakon tri godine:", round(FVgov3))


elif(izbor == 3): # Predviđanje količine uroda nekog trajnog nasada za sljedeću godinu
   
    print("Predviđanje uroda za trajni nasad za iduću godinu")
    print("----------------------------------------------------------------------------------------------")
     
    # Učitavanje odabira trajnog nasada od korisnika
    trajni_nasad = input("Unesite ime trajnog nasada: ")
    
    # Učitavanje postotka očekivanog prinosa za svaku opciju
    
    postotak = float(input("Koliko posto očekujete prinosa za {}? Unesite decimalni broj: ".format(trajni_nasad)))
   
    # Učitavanje uroda od prošle godine
    urod = int(input("Koliko je bilo ukupno uroda od prošle godine? Unesite mjeru u tonama): "))

    # Računanje očekivanog prinosa za svaku opciju
    print("Očekivani prinos za {}:".format(trajni_nasad))
    prinos = round(urod * (postotak / 100), 2)
    print("- {} : {} tona".format(trajni_nasad, prinos))




elif(izbor == 4): #Usporedba poljoprivredne površine za 2013. i 2016 godinu
    
    print("Usporedba poljoprivredne površine za 2013. i 2016 godinu")
    print("----------------------------------------------------------------------------------------------")
    
    # Definirajte izbornika sa županijama
    zupanije = {
        "1": "Zagrebačka",
        "2": "Krapinsko-zagorska",
        "3": "Sisačko-moslavačka",
        "4": "Karlovačka",
        "5": "Varaždinska",
        "6": "Koprivničko-križevačka",
        "7": "Bjelovarsko-bilogorska",
        "8": "Primorsko-goranska",
        "9": "Ličko-senjska",
        "10": "Virovitičko-podravska",
        "11": "Požeško-slavonska",
        "12": "Brodsko-posavska",
        "13": "Zadarska",
        "14": "Osječko-baranjska",
        "15": "Šibensko-kninska",
        "16": "Vukovarsko-srijemska",
        "17": "Splitsko-dalmatinska",
        "18": "Istarska",
        "19": "Dubrovačko-neretvanska",
        "20": "Međimurska"
    }

    # Ispis izbornika sa županijama
    print("Odaberite županiju:")
    for k, v in zupanije.items():
        print(k + ". " + v)

    # Unos korisnikovog odabira
    odabir = input("Unesite broj županije: ")

    # Provjera ispravnosti korisnikovog odabira
    if odabir in zupanije.keys():
        zupanija = zupanije[odabir]
        print("Odabrali ste županiju " + zupanija + ".")
    else:
        print("Krivi unos.")
        
    zemlja = int(input("Upišite površinu poljoprivredne površine odabrane županije za 2013. godinu (U km kvadratnima): "))
        
    prvooc = float(input("Koliko je bilo vaše predviđanje za 2014. godinu? Unesite decimalni broj: "))
    drugooc = float(input("Koliko je bilo vaše predviđanje za 2015. godinu? Unesite decimalni broj: "))
    treceoc = float(input("Koliko je bilo vaše predviđanje za 2016. godinu? Unesite decimalni broj: "))    
    
    ukupnopost = prvooc + drugooc + treceoc
    
    rezul = zemlja * ukupnopost
    
    print("Vaše očekivanje za 2016. godinu je: {}".format(rezul))
    
else:
    print("Neispravan unos!\n")
    goto: natrag
