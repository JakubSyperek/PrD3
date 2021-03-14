import math
def prostokatny(a,b,c):
    if (a**2 + b**2 == c**2) or (a**2 + c**2 == b**2) or (b**2 + c**2 == a**2):
        print("Trójkąt ten jest prostokątny.")
    else:
        print("Trójkąt ten nie jest prostokątny.")

a = float(input("Podaj długość pierwszego boku: "))
b = float(input("Podaj długość drugiego boku: "))
c = float(input("Podaj długość trzeciego boku: "))
prostokatny(a,b,c)

