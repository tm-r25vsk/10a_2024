# 1. Uzdevums: Celsius uz Fahrenheit pārveidotājs
# Izveido funkciju, kas pārvērš temperatūru no Celsija uz Fārenheitu. 

def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    return fahrenheit

# Piemērs
celsius = 25
print(f"{celsius}°C = {celsius_to_fahrenheit(celsius):.2f}°F")
# Izvade:
# 25°C = 77.00°F
# ________________________________________

# 2. Uzdevums: Vidējā skaitļa aprēķins
# Izveido funkciju, kas aprēķina trīs skaitļu aritmētisko vidējo.

def calculate_average(a, b, c):
    average = (a + b + c) / 3
    return average

# Piemērs
num1, num2, num3 = 10, 20, 30
print(f"Vidējais no {num1}, {num2}, {num3} ir {calculate_average(num1, num2, num3):.2f}")
# Izvade:
# Vidējais no 10, 20, 30 ir 20.00
# ________________________________________

# 3. Uzdevums: Palindroma pārbaude
# Izveido funkciju, kas pārbauda, vai dotā simbolu virkne ir palindroms (lasa vienādi no abiem galiem).

def is_palindrome(word):
    word = word.lower().replace(" ", "")  # Ignorē lielos burtus un atstarpes
    return word == word[::-1]

# Piemērs
text = "level"
print(f"Vai '{text}' ir palindroms? {'Jā' if is_palindrome(text) else 'Nē'}")

# Vai 'level' ir palindroms? Jā
# ________________________________________

# 4. Uzdevums: Maksimālā vērtība
# Izveido funkciju, kas atrod un atgriež lielāko vērtību no trīs ievadītajiem skaitļiem.

def find_maximum(a, b, c):
    maximum = max(a, b, c)
    return maximum

# Piemērs
num1, num2, num3 = 15, 25, 10
print(f"Lielākais skaitlis no {num1}, {num2}, {num3} ir {find_maximum(num1, num2, num3)}")
# Izvade:

# Lielākais skaitlis no 15, 25, 10 ir 25
# ________________________________________

# 5. Uzdevums: Skaitļa faktoriāls
# Izveido funkciju, kas aprēķina dotā skaitļa faktoriālu. 

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Piemērs
number = 5
print(f"{number}! = {factorial(number)}")
# Izvade:

# 5! = 120

