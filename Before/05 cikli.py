import os 
os.system('cls') # attīra termināla logu pašā sākumā
print("\n")  # ieliek tukšu rindiņu pirms izdrukas 

# https://learning.edx.org/course/course-v1:HarvardX+CS50P+Python/block-v1:HarvardX+CS50P+Python+type@sequential+block@59c86cd0b84f463d814d6fd46a2c7eea/block-v1:HarvardX+CS50P+Python+type@vertical+block@d030524223b84aaa86e5306856d4b028?_gl=1%2A1fglmvv%2A_gcl_au%2ANzM0Mjk2NTg3LjE3MjU5NzE1MDU.%2A_ga%2AMjkwODg2MTEwLjE3MjU5NzE0ODI.%2A_ga_D3KS4KMDT0%2AMTczMjA5NTg1Ny4yNi4xLjE3MzIwOTU4NzUuNDIuMC4w

print("Es esmu gudrs")
print("Es esmu gudrs")
print("Es esmu gudrs")

# zīmejam vienkāršu blokshēmu
# kā vienkāršāk attkārtot vienādas vai līdzīgas komandas?

# while

i = 3
while i != 0:
    print("Es esmu gudrs") 
    # bez i maiņas atkārtosies bezgalīgi CTRL+C
    i = i - 1
    # zīmejam blokshēmu
    
i = 1
while i <= 3:
    print("Es esmu gudrs") 
    i = i + 1

# lielākā daļa programmētāju sāk skaitīt no 0

i = 0
while i < 3:
    print("Es esmu gudrs") 
    i += 1

# Uzdevums.
# Programma, kas modelē metamā kauliņa mešanu 50 reizes un saskaita, cik reižu uzmests "6". 
# Tajā tiek izmantots modulis random nejaušu skaitļu ģenerēšanai.

import random

# Metamā kauliņa attēli
kaulins = {
    1: "-----\n|   |\n| ● |\n|   |\n-----",
    2: "-----\n|●  |\n|   |\n|  ●|\n-----",
    3: "-----\n|●  |\n| ● |\n|  ●|\n-----",
    4: "-----\n|● ●|\n|   |\n|● ●|\n-----",
    5: "-----\n|● ●|\n| ● |\n|● ●|\n-----",
    6: "-----\n|● ●|\n|● ●|\n|● ●|\n-----"
}

# Rezultātu saglabāšana
rezultati = []
skaits_6 = 0
metienu_skaits = 0

# Metamā kauliņa mešana ar while
while metienu_skaits < 50:
    metiens = random.randint(1, 6)  # Ģenerē nejaušu skaitli no 1 līdz 6
    rezultati.append(metiens)
    if metiens == 6:
        skaits_6 += 1
    metienu_skaits += 1

    # Izvada metamā kauliņa attēlu
    print(f"Metiens {metienu_skaits}:")
    print(kaulins[metiens])
    print()

# Izvade
print("Visi metienu rezultāti:", rezultati)
print(f"Sešinieks uzmests {skaits_6} reizes.")

# v.2 bez rezultātu saglabāšanas:

import random

# Rezultātu saglabāšana
skaits_6 = 0
metienu_skaits = 0

# Metamā kauliņa mešana ar while
while metienu_skaits < 50:
    metiens = random.randint(1, 6)  # Ģenerē nejaušu skaitli no 1 līdz 6
    if metiens == 6:
        skaits_6 += 1
    metienu_skaits += 1

# Izvade
print(f"Sešinieks uzmests {skaits_6} reizes.")




# for
# list 

for i in [0, 1, 2]:
    print("Es esmu gudrs")  # ļoti slikti rakstās lielām vērtībām
    
# var izmantot "range" funkciju

for i in range(3):
    print("Es esmu gudrs")

# mainīgā i vietā var izmantot "_", ja nav svarīgs mainīgā vārds

for _ in range(3):
    print("Es esmu gudrs")


# vēl viens variants kā atkārtot:

print("Es vēl joprojām esmu gudrs " * 3)
print("Es vēl joprojām esmu gudrs\n" * 3, end="")  # "end" izņem pēdējo tukšo rindu


# Lai izbēgtu no nevajadzīgiem/nepareiziem/liekiem ievaddatiem:

while True:
    n = int(input("Cik reizes? "))
    if n < 0:
        continue
    else:
        break

# Vai vēl labāk:

while True:
    n = int(input("Cik reizes? "))
    if n > 0:
        break

for _ in range(n):
    print("Esmu gudrs")
    
# https://video.cs50.io/-7xg8pGcP6w?start=2134 35 min