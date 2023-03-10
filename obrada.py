import pandas as pd
import numpy as np
import random as rnd

pod2013 = pd.read_excel('data.xlsx', sheet_name = "2013")
pod2014 = pd.read_excel('data.xlsx', sheet_name = "2014")
pod2015 = pd.read_excel('data.xlsx', sheet_name = "2015")
pod2016 = pd.read_excel('data.xlsx', sheet_name = "2016")

# Ispis podataka
print("2013.")
print(pod2013) # Prikaz svih podataka 2013. godine
print("\n-----------------------------------------------------------------\nDetalji\n", pod2013.iloc[ : , 1 : ].describe()) # Detaljna analiza 2013.
print("2014.")
print(pod2013) # Prikaz svih podataka 2013. godine
print("\n-----------------------------------------------------------------\nDetalji\n", pod2014.iloc[ : , 1 : ].describe()) # Detaljna analiza 2014.
print("2015.")
print(pod2013) # Prikaz svih podataka 2013. godine
print("\n-----------------------------------------------------------------\nDetalji\n", pod2015.iloc[ : , 1 : ].describe()) # Detaljna analiza 2015.
print("\n\n2016.")
print(pod2016) # Prikaz svih podataka 2016. godine
print("\n-----------------------------------------------------------------\nDetalji\n", pod2016.iloc[ : , 1 : ].describe()) # Detaljna analiza 2016.
print("\n")

pod2013_lista = pod2013.values.tolist()
pod2016_lista = pod2016.values.tolist()
det2013 = pod2013.iloc[ : , 1:].describe() # Varijable detaljnih podataka za kasnije korištenje
det2016 = pod2016.iloc[ : , 1:].describe()
#print(pod2013_lista[][]]) # Debug (provjera selekcije podataka)
#print(pod2016_lista[][]])

natrag: print("Izbornik\n\n1 - Promjena poljoprivredne površine\n2 - Promjena količine goveda\n3 - Predviđanje uroda za trajni nasad za iduću godinu\n4 - Usporedba poljoprivredne površine za 2013. i 2016 godinu")
izbor = int(input("Unesite izbor: "))
print()

if(izbor == 1): # Računanje porasta iskorištene poljoprivredne površine

    print("Porast iskorištene poljoprivredne površine")
    print("----------------------------------------------------------------------------------------------")

    rnd.seed()
    PV = pod2013_lista[1][1] # Vrijednost poljoprivredne površine u RH tokom 2013. godine
    r = float(rnd.uniform(1, 10)) # Nasumično odabrana "kamatna stopa" rasta
    n = 3 # Razdoblje 2013. - 2016.
    FV = PV * (r / 100) ** n

    # Izračunaj povećanje u odnosu na početnu vrijednost
    porast = FV - PV

    # Izračunaj vjerojatnost povećanja
    vjerojatnost = porast / PV

    # Ispiši rezultate
    print("Stopa rasta:", r, "%")
    print("Buduća vrijednost poljoprivredne površine nakon dvije godine:", FV, "metara kvadratnih")
    
    if porast > 0:
        print("Povećanje poljoprivredne površine u odnosu na početnu vrijednost:", porast, "metara kvadratnih")
    else:
        print("Smanjenje poljoprivredne površine u odnosu na početnu vrijednost:", -porast, "metara kvadratnih")
    
    print("Vjerojatnost povećanja poljoprivredne površine u sljedeće dvije godine:", vjerojatnost, "%")
    print()


elif(izbor == 2): # Predviđanje količine goveda nakon 3 godine

    print("Promjena količine goveda")
    print("----------------------------------------------------------------------------------------------")

    PVgov = pod2016_lista[1][8] # Broj goveda u RH 2016. godine
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
    print(pod2013.Zupanija)
    
    # Unos korisnikovog odabira
    odabir = input("Unesite broj županije: ")

    # Provjera ispravnosti korisnikovog odabira
    if odabir in pod2013['Zupanija'].index:
        zupanija = pod2013.Zupanija[odabir]
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
