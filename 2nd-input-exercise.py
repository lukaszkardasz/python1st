'''Stwórz program, który prosi użytkownika o podanie imienia, wieku i ulubiony kolor.

Wypisz wartości w przyjemny dla oka sposób. Wypisz ile lat ma użytkownik oraz ile lat będzie miał za rok.

Przykład:

#Dane podawane w konsoli:
Podaj swoje imię: Arek
Podaj swój wiek: 30
Podaj swój ulubiony kolor: niebieski
 
#WYNIK:
Hej Arek, Twój ulubiony kolor to niebieski
Masz 30 lat.
Za rok będziesz miał 31 lat.
'''

# Step 1: Prompt the user for inputs
name = input("Podaj swoje imię: ")
age = int(input("Podaj swój wiek: "))
favorite_color = input("Podaj swój ulubiony kolor: ")

# Step 2: Print the values in a user-friendly format
print(f"Hej {name}, Twój ulubiony kolor to {favorite_color}")
print(f"Masz {age} lat.")
print(f"Za rok będziesz miał {age + 1} lat.")