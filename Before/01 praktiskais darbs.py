# import locale
import math

# 1. Simbolu virknes garums
string = input("Ievadi simbolu virkni: ")
print(f"Simbolu virknes garums: {len(string)}")

# 2. Virknes pārveidošana uz lielajiem vai mazajiem burtiem
print(f"Virkne ar lielajiem burtiem: {string.upper()}")
print(f"Virkne ar mazajiem burtiem: {string.lower()}")

# 3. Aizvietot rakstzīmi simbolu virknē
symbol = input("Ievadi simbolu, ko lietot tukšo vietu aizvietošanai: ")
print(f"Aizvietotas atstarpes: {string.replace(' ', symbol)}")

# 4. Pārbaudīt, vai virkne satur noteiktu vārdu
word_to_check = "Python"
print(f"Vai virkne satur vārdu '{word_to_check}'? {'Python' in string}")

# 5. Griezt simbolu virkni
print(f"Pirmie pieci simboli: {string[:5]}")
print(f"Pēdējie trīs simboli: {string[-3:]}")

# 6. Skaitļa noapaļošana līdz noteiktam ciparam aiz komata
number = float(input("Ievadi skaitli: "))
print(f"Skaitlis noapaļots līdz diviem cipariem aiz komata: {round(number, 2)}")

# 7. Skaitļa pārveidošana par decimāldaļu
integer = int(input("Ievadi veselu skaitli: "))
print(f"Skaitlis kā decimāldaļa: {float(integer)}")

# 8. Skaitļa formāta maiņa (tūkstošu atdalītājs)
large_number = int(input("Ievadi lielu skaitli: "))
print(f"Skaitlis ar tūkstošu atdalītāju: {large_number:,}".replace(',', ' '))

# 9. Skaitļa pārveidošana uz bināro, oktālo un heksadecimālo sistēmu
print(f"Skaitlis binārajā sistēmā: {bin(integer)[2:]}")
print(f"Skaitlis oktālajā sistēmā: {oct(integer)[2:]}")
print(f"Skaitlis heksadecimālajā sistēmā: {hex(integer)[2:]}")

# 10. Skaitļu absolūtās vērtības aprēķināšana
negative_number = int(input("Ievadi negatīvu skaitli: "))
print(f"Absolūtā vērtība: {abs(negative_number)}")

# Papildus uzdevumi

# Vārdu skaits simbolu virknei
words = string.split()
print(f"Vārdu skaits virknei: {len(words)}")

# Skaitļa kvadrātsakne
sqrt_number = float(input("Ievadi skaitli kvadrātsaknes aprēķināšanai: "))
print(f"Skaitļa kvadrātsakne: {math.sqrt(sqrt_number)}")

# Matemātiskās konstantes (pi) izdrukāšana ar precizitāti līdz četrām decimāldaļām
print(f"Matemātiskā konstante pi: {math.pi:.4f}")
