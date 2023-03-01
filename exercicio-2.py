qtd = int(input())

a = 0
b = 1
c = 1

lista = []

lista.append(a)
lista.append(b)

print(a)
print(a , b, end=' ')
for numero in range(qtd):
    c = b + a
    lista.append(c)
    print(c, end=" ")
    a = b
    b = c

print()

print(lista)
if qtd in lista:
    print("Pertence à sequência")
else:
    print("não pertence à sequencia")