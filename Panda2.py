import pandas as pd

df = pd.read_excel('Teste.xlsx')

#Filtrando items

#Escolhendo apartir de uma lista
#print(df.filter(['FirstName', 'LastName']).head())

#Escolhendo items que contem uma string
#print(df.filter(like='Name').head())

#O mesmo de antes porem mais complexo. Exemplo: [0-9] + 'Name', vai procurar por numeros de 0 a 9 no comeco e depois procurar por esses que tambem tenha Name
#print(df.filter(regex='[a-b]+Name').head())


print(df.head())
