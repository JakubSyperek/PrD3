#a = float(input("Podaj długość pierwszej podstawy: "))
#b = float(input("Podaj długość drugiej podstawy: "))
#h = float(input("Podaj wysokość: "))
def pole(a,b,h):
    p = (((a + b)*h)/2)
    if a > 0 or b > 0 or c > 0:
        print("Pole:")
        return p
    else:
        print("Nieprawidłowe dane.")
print(pole(6,1,2))
print(pole(2,3,4))
print(pole(-1,2,3))