# Programma atrisina kvadrātvienādojumu.
# Kvadrātvienādojuma standarta forma ir ax2+bx+c=0,
# aprēķinām diskriminantu D=b2-4ac un izmantojam to, lai noteiktu risinājumus.

import os 
os.system('cls') # attīra termināla logu pašā sākumā
print("\n")  # ieliek tukšu rindiņu pirms izdrukas 

# import math

# # Koeficienti
# a = float(input("Ievadiet koeficientu a: "))
# b = float(input("Ievadiet koeficientu b: "))
# c = float(input("Ievadiet koeficientu c: "))

# # Diskriminanta aprēķināšana
# D = b**2 - 4 * a * c

# # Risinājumu noteikšana, balstoties uz diskriminanta vērtību
# if D > 0:
#     x1 = (-b + math.sqrt(D)) / (2 * a)
#     x2 = (-b - math.sqrt(D)) / (2 * a)
#     print(f"Divas reālas saknes: x1 = {x1}, x2 = {x2}")
# elif D == 0:
#     x = -b / (2 * a)
#     print(f"Vienīga reāla sakne: x = {x}")
# else:
#     print(f"Vienādojumam ar koeficientiem a = {a}, b = {b}, c = {c} nav reālu sakņu")
#     real_part = -b / (2 * a)
#     imaginary_part = math.sqrt(-D) / (2 * a)
#     print(f"Divas kompleksas saknes: x1 = {real_part} + {imaginary_part}i, x2 = {real_part} - {imaginary_part}i")


# ==========================================================

# Gads ir garais gads, ja tas dalās ar 4, izņemot gadus, kas dalās ar 100, bet nedalās ar 400.

gads = int(input("Gads? " ))

if gads % 4 == 0:
    if gads % 100 == 0:
        if gads % 400 == 0:
            print(gads, "ir garais gads.")
        else:
            print(gads, "nav garais gads.")
    else:
        print(gads, "ir garais gads.")
else:
    print(gads, "nav garais gads.")