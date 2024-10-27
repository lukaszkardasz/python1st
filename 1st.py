from math import sqrt
import pathlib


text = sqrt(4)
print(text)

print("Aktualna ścieżka: " + str(pathlib.Path.cwd()))

imie = ("Łukasz")

imie = imie.upper()
print(imie)

a = int(input("Podaj liczbę a: "))
print("liczba a:",a)

b = int(input("Podaj liczbę b: "))
print("liczba b:", b)

print("wynik dodawania", a, " + ", b, "=",  a + b)