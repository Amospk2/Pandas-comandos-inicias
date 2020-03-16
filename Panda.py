import pandas as pd


#Dados = pd.read_excel('Teste.xlsx', usecols=['UserId'])

Dados = pd.read_excel('Teste.xlsx')

#print(Dados.head())

#Adicionar coluna
#Dados['NomeInteiro'] = Dados['FirstName'] + ' ' + Dados['MidName'] + ' ' + Dados['LastName']

#escolher item especifico
#print(Dados['FirstName'][0])

#Mudar item...
'''

Dados['UserId'][0] = '123'
'''
'''
#Escolhendo Linhas e Colunas, pode usar o nome da coluna
print(Dados.loc[[1, 2], 'FirstName':'LastName'])

print()

#nao pode usar o nome da coluna + nao pega o ultimo se for por indice: 1:4 nao pega o 4
print(Dados.iloc[[0, 3], 0:])
'''
print(Dados.head())


