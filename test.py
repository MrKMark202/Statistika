import pandas as pd

df = pd.read_excel('data.xlsx', sheet_name = 'podaci')

df.values.tolist()

print(df["Broj poljoprivrednih gospodarstava"])
print(df["Koristena poljoprivredna povrsina, ha"])
print(df["Zitarice"])
print(df["Secerna repa"])
print(df["Povrtnjaci"])
print(df["Trajni nasadi"])
print(df["Vocnjaci"])
print(df["Goveda"])


Number_of_agricultural_holdings = [print(df["Broj poljoprivrednih gospodarstava"])]