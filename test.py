import pandas as pd

podaci = pd.read_excel('data.xlsx')

print(podaci) # Prikaz svih podataka
print("\n")

podaci_u_listu = podaci.values.tolist()
#print(podaci_u_listu[][]]) # Debug (provjera selekcije podataka)

print("Izbornik\n\n1 - Promjena poljoprivredne površine\n2 - Promjena količine goveda")
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
    