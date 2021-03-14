import random

a = random.randint(0,100)
b = random.randint(0,100)
c = random.randint(0,100)
d = random.randint(0,100)
e = random.randint(0,100)
f = random.randint(0,100)
g = random.randint(0,100)
h = random.randint(0,100)
i = random.randint(0,100)
j = random.randint(0,100)

lista = []
lista.insert(1,a)
lista.insert(1,b)
lista.insert(1,c)
lista.insert(1,d)
lista.insert(1,e)
lista.insert(1,f)
lista.insert(1,g)
lista.insert(1,h)
lista.insert(1,i)
lista.insert(1,j)
print(lista)

parzyste = []

for i in lista:
    if i % 2 == 0:
        parzyste.append(i)
print("Liczby parzyste:")
print(parzyste)
print()