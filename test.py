import pandas as pd

podaci = pd.read_excel('data.xlsx')

print(podaci) # Prikaz svih podataka
print("\n")

podaci_u_listu = podaci.values.tolist()

# Računanje porasta iskorištene poljoprivredne površine
print("Porast iskorištene poljoprivredne površine")
print("----------------------------------------------------------------------------------------------")
PV = podaci_u_listu[1][1] # Vrijednost poljoprivredne površine u RH tokom 2013. godine
r = 0.5
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