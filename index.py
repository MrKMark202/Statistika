import pandas as pd
import openpyxl 

data = pd.read_excel(r'E:\GitHub\Statistika\poljoprivreda-pregled-po-zupanijama.xlsx') 

df = pd.read_excel(r'E:\GitHub\Statistika\poljoprivreda-pregled-po-zupanijama.xlsx', sheet_name='1.2.1.')
#print(df)

#df = pd.read_excel("poljoprivreda-pregled-po-zupanijama.xlsx", skiprows = [ i for i in range(8, 31, 1) ]  ) 

#print(df)

df = pd.read_excel('data.xlsx')

print(df)

 
Number_of_agricultural_holdings = []
Utilised_agricultural_area = []
Cereals = []
Sugar_beet = []
Kitcher_garden = []
Permanent_crops = []
Vocnjaci = []
Cattle = []

Number_of_agricultural_holdings = pd.DataFrame(data = 'C')
print(Number_of_agricultural_holdings)

Utilised_agricultural_area = pd.DataFrame(data, colum=['D'])
print(Utilised_agricultural_area)

Cereals = pd.DataFrame(data, columns=['E'])
print(Number_of_agricultural_holdings)

Sugar_beet = pd.DataFrame(data, columns=['F'])
print(Number_of_agricultural_holdings)

Kitcher_garden = pd.DataFrame(data, columns=['G'])
print(Number_of_agricultural_holdings)

Permanent_crops = pd.DataFrame(data, columns=['H'])
print(Number_of_agricultural_holdings)

