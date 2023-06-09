import pandas as pd
import numpy as np
import random as rnd
import matplotlib.pyplot as plt
import csv


pod2013 = pd.read_excel('data.xlsx', sheet_name = "2013")
pod2014 = pd.read_excel('data.xlsx', sheet_name = "2014")
pod2015 = pd.read_excel('data.xlsx', sheet_name = "2015")
pod2016 = pd.read_excel('data.xlsx', sheet_name = "2016")
det2013 = pod2013.iloc[ : , 1 : ].describe() # Varijable detaljnih podataka za kasnije korištenje
det2014 = pod2014.iloc[ : , 1 : ].describe()
det2015 = pod2015.iloc[ : , 1 : ].describe()
det2016 = pod2016.iloc[ : , 1 : ].describe()

# Ispis podataka
print("2013.")
print(pod2013) # Prikaz svih podataka 2013. godine
print("\n---------------------------------------------------------------------\nDetalji\n", det2013) # Detaljna analiza 2013.
print("\n\n2014.")
print(pod2013) # Prikaz svih podataka 2013. godine
print("\n---------------------------------------------------------------------\nDetalji\n", det2014) # Detaljna analiza 2014.
print("\n\n2015.")
print(pod2013) # Prikaz svih podataka 2013. godine
print("\n---------------------------------------------------------------------\nDetalji\n", det2015) # Detaljna analiza 2015.
print("\n\n2016.")
print(pod2016) # Prikaz svih podataka 2016. godine
print("\n---------------------------------------------------------------------\nDetalji\n", det2016) # Detaljna analiza 2016.
print("\n")

pod2013_lista = pod2013.values.tolist()
pod2014_lista = pod2014.values.tolist()
pod2015_lista = pod2015.values.tolist()
pod2016_lista = pod2016.values.tolist()

# Debug (provjera selekcije podataka)
#print(pod2013_lista[][])
#print(pod2014_lista[][])
#print(pod2015_lista[][])
#print(pod2016_lista[][])

natrag: print("Izbornik\n\n1 - Promjena poljoprivredne površine\n2 - Promjena količine goveda\n3 - Predviđanje uroda za trajni nasad za iduću godinu\n4 - Usporedba poljoprivredne površine za 2013. i 2016 godinu")
izbor = int(input("Unesite izbor: "))
print()

if(izbor == 1): # Računanje porasta iskorištene poljoprivredne površine

    print("Porast iskorištene poljoprivredne površine")
    print("----------------------------------------------------------------------------------------------")

    rnd.seed()
    PV = pod2013_lista[1][1] # Vrijednost poljoprivredne površine u RH tokom 2013. godine
    r = "{:.2f}".format(float(rnd.uniform(1, 10))) # Nasumično odabrana "kamatna stopa" rasta
     
    n = 3 # Razdoblje 2013. - 2016.
    FV = PV * (float(r) / 100) ** n

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
    rođeno = float(rnd.uniform(1, 10))
    uginulo = float(rnd.uniform(1, 10))
    
    # Zaokruživanje decimalnog broja na 2 znamenke
    ro = "{:.2f}".format(rođeno)
    ug = "{:.2f}".format(uginulo)

    FVgov1 = PVgov + rođeno - uginulo # Prva godina
    FVgov2 = FVgov1 + rođeno - uginulo # Druga godina
    FVgov3 = FVgov2 + rođeno - uginulo # Treća godina

    print("Stopa rodnosti goveda: ", ro, "%")
    print("Stopa smrtnisti goveda: ", ug, "%")
    print("Broj goveda nakon tri godine:", round(FVgov3))


elif(izbor == 3): # Predviđanje količine uroda nekog trajnog nasada za sljedeću godinu
   
    print("Predviđanje uroda za trajni nasad za iduću godinu")
    print("----------------------------------------------------------------------------------------------")
     
    # Učitavanje odabira trajnog nasada od korisnika
    trajni_nasad = input("Unesite ime trajnog nasada: ")
    
    # Učitavanje postotka očekivanog prinosa za svaku opciju
    
    postotak = float(rnd.uniform(1, 10))
    format_float = "{:.2f}".format(postotak)
   
    # Učitavanje uroda od prošle godine
    urod = int(input("Koliko je bilo ukupno uroda od prošle godine? Unesite mjeru u tonama): "))

    # Računanje očekivanog prinosa za svaku opciju
    print("Postotak uroda predviđen za iduću godinu: ",format_float, "%")
    print("Očekivani prinos za {}:".format(trajni_nasad))
    prinos = round(urod * (postotak / 100), 2)
    print("- {} : {} tona".format(trajni_nasad, prinos))


elif(izbor == 4): #Usporedba poljoprivredne površine za 2013. i 2016 godinu
    
    print("Usporedba poljoprivredne površine za 2013. i 2016 godinu")
    print("----------------------------------------------------------------------------------------------")
    
   
    zemlja = int(input("Upišite površinu poljoprivredne površine odabrane županije za 2013. godinu (U km kvadratnima): "))
        
    prvooc = float(rnd.uniform(-10, 10))
    drugooc = float(rnd.uniform(-10, 10))
    treceoc = float(rnd.uniform(-10, 10))
    
    p = "{:.2f}".format(prvooc)
    d = "{:.2f}".format(drugooc)
    t = "{:.2f}".format(treceoc)
    
    ukupnost = float
    rezul = float
    
    ukupnopost = prvooc + drugooc + treceoc
    uk = "{:.2f}".format(ukupnopost)
    
    rezul = zemlja * ukupnopost
    r = "{:.2f}".format(rezul)
    
    print("Postotak za prvu godinu", p, "%")
    print("Postotak za drugu godinu", d, "%")
    print("Postotak za treću godinu", t, "%")
    
    print("Vaše očekivanje za 2016. godinu je: ", r)

elif(izbor == 5): # Grafovi
    plt.hist(pod2013["Broj poljoprivrednih gospodarstava"], alpha = 0.5, label = "2013")
    plt.hist(pod2014["Broj poljoprivrednih gospodarstava"], alpha = 0.5, label = "2014")
    plt.hist(pod2015["Broj poljoprivrednih gospodarstava"], alpha = 0.5, label = "2015")
    plt.hist(pod2016["Broj poljoprivrednih gospodarstava"], alpha = 0.5, label = "2016")
    plt.legend(loc = "upper right")
    plt.show()
    
else:
    print("Neispravan unos!\n")
    goto: natrag
    


from PIL import Image

ntrag: print("Izbornik\n\n1 - Graf za polj. površinu za 2013. godinu\n2 - Graf za polj. površinu za 2014. godinu\n3 - Graf za polj. površinu za 2015. godinu\n4 - Graf za polj. površinu za 2016. godinu\n5 - Graf koji uspoređuje polj. površine kroz sve 4 godine")
izbr = int(input("Unesite izbor: "))
print()
    
if(izbr==1):
    img = Image.open("2013 graf.png")
    img.show()

elif(izbr==2):
    img = Image.open("2014 graf.png")
    img.show()
    
elif(izbr==3):
    img = Image.open("2015 graf.png")
    img.show()
    
elif(izbr==4):
    img = Image.open("2016 graf.png")
    img.show()
    
elif(izbr==5):
    img = Image.open("Linijski graf.png")
    img.show()

else:
    print("Neispravan unos!\n")
    goto: ntrag




import numpy as np
import matplotlib.pyplot as plt

var1 = []
var2 = []
var3 = []
var4 = []
var5 = []
var6 = []
var7 = []
var8 = []
var9 = []
var10 = []

# generiraj slučajne podatke
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

for l in range(10):
     var1 = int(rnd.uniform(25, 50))
     var2 = int(rnd.uniform(25, 50))
     var3 = int(rnd.uniform(25, 50))
     var4 = int(rnd.uniform(25, 50))
     var5 = int(rnd.uniform(25, 50))
     var6 = int(rnd.uniform(25, 50))
     var7 = int(rnd.uniform(25, 50))
     var8 = int(rnd.uniform(25, 50))
     var9 = int(rnd.uniform(25, 50))
     var10 = int(rnd.uniform(25, 50))
     
y = np.array([var1, var2, var3, var4, var5, var6, var7, var8, var9, var10])

# izračunaj koeficijente regresije
b1, b0 = np.polyfit(x, y, 1)

# nacrtaj graf
plt.scatter(x, y)
plt.plot(x, b1 * x + b0, color='red')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()




#Računanje uroda trajnih nasada za 2017. godinu preko jednadžbe regresijskog pravca


suma_x = 10
suma_y = 289.10
suma_xy = 724.36
suma_x_na_kvadrat = 30

bbb = (4 * suma_xy - suma_x * suma_y) / (4 * suma_x_na_kvadrat - (suma_x*suma_x))
aaa = (suma_y - (-bbb) * suma_x) / 4

banana = aaa - bbb * 5

x = np.array([2013, 2014, 2015, 2016, 2017])

vari1 = 72.94
vari2 = 72.25
vari3 = 71.94
vari4 = 71.97
vari5 = banana

     
y = np.array([vari1, vari2, vari3, vari4, vari5])

# izračunaj koeficijente regresije
b1, b0 = np.polyfit(x, y, 1)

# nacrtaj graf
plt.scatter(x, y)
plt.plot(x, b1 * x + b0, color='red')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()