#def ciag(*liczby):
#    if len(liczby) == 0:
#        return 0
#    else:
#        suma = 0
#    for a, b, ile in liczby:
#        suma == a * (b**(ile-1))
#    return suma
#print(ciag())
#print(ciag(1, 4, 10))

def ciag(*liczby):
    if len(liczby) == 0:
        return 0
    else:
        suma = 0
    for i in liczby:
        suma += i
    return suma
print(ciag())
print(ciag(1, 2, 3.5, 4, 5, 6, 7, 8))