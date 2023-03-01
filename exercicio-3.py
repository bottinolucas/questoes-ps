import json

#abrindo os dados do json 
with open("dados.json") as json_analisado:
    dados = json.load(json_analisado)

 #criando lista para separar os valores necessários
lista_valores = []

#iterando para adicionar os faturamentos diários
for i in dados:
    lista_valores.append(i["valor"])

numero = 0.0

#removendo os dias sem faturamento
while numero in lista_valores:
    lista_valores.remove(numero)

#organizando a lista
lista_valores.sort()

#print(lista_valores)

#output do menor e do maior valor da lista

print(f'O menor valor de faturamento obtido no mês foi {min(lista_valores)} R$')
print(f'O maior valor de faturamento obtido no mês foi {max(lista_valores)} R$')

#somando todos os elementos da lista e calculando a média
soma = 0

for numero in lista_valores:
    soma = soma + numero

#print(soma)
#print(len(lista_valores))
media = soma/len(lista_valores)
#print(f'{media}')

#for value in lista_valores:
#    if media > value:
#        lista_valores.remove(value)
#print(lista_valores)

lista_nova = []

for value in lista_valores:
    if value > media:
        lista_nova.append(value)
print(f'Total de dias do mês em que o valro de faturamento diário foi superior à média mensal: {len(lista_nova)} dias')