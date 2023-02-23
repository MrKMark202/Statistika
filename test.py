import pandas as pd

df = pd.read_excel('data.xlsx', sheet_name='podaci')

df.values.tolist()

print(df["Broj poljoprivrednih gospodarstava"])
print(df["Koristena poljoprivredna povrsina, ha"]) 
print(df["Zitarice"]) 
print(df["Secerna repa"]) 
print(df["Povrtnjaci"]) 
print(df["Trajni nasadi"]) 
print(df["Vocnjaci"]) 
print(df["Goveda"]) 

print(df["Broj poljoprivrednih gospodarstava2"])
print(df["Koristena poljoprivredna povrsina, ha2"]) 
print(df["Zitarice2"]) 
print(df["Secerna repa2"]) 
print(df["Povrtnjaci2"]) 
print(df["Trajni nasadi2"]) 
print(df["Vocnjaci2"]) 
print(df["Goveda2"]) 


print(df["2013.", "Vocnjaci"])