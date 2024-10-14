import os 
os.system('cls') # attīra termināla logu pašā sākumā
print("\n")  # ieliek tukšu rindiņu pirms izdrukas 

x = int(input("Kāda ir x vērtība? "))
y = int(input("Kāda ir y vērtība? "))

if x < y:
    print("x ir mazāks par y")
    
# ====================================
# turpinājums pēc ievada:

if x > y:
    print("x ir lielāks par y")
if x == y:
    print("x ir vienāds ar y")