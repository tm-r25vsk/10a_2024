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
        
# Blokshēma nr.1 ar skaidrojumu
# Vai programma strādā pareizi - jā
# Vai tā ir skaista - nē    
# Varam izveidot skaitāku dizainu - elif    
# programma adarbosies tālāk tikai tad, ja iepriekšējais apgalvojums nebūs pareizs 

# elif
   
if x < y:
    print("x ir mazāks par y")
elif x > y:
    print("x ir lielāks par y")
elif x == y:
    print("x ir vienāds ar y")    

# Blokshēma nr.2 ar skaidrojumu    

# Vai programma strādā pareizi - jā
# Vai tā ir skaista - ir labāka   
# Varam izveidot skaitāku dizainu - elif + else

# else

if x < y:
    print("x ir mazāks par y")
elif x > y:
    print("x ir lielāks par y")
else:
    print("x ir vienāds ar y")  

# Blokshēma nr.3 ar skaidrojumu    
    

# ja var apmierināties ar vienkāršākiem skaidrojumiem, var izmantot or

x = int(input("Kāda ir x vērtība? "))
y = int(input("Kāda ir y vērtība? "))

if x < y or x > y:
    print("x nav vienāds ar y")
else:
    print("x ir vienāds ar y")

# Blokshēma nr.4 ar skaidrojumu
# Vai var uzlabot vēl - !=

if x != y:
    print("x nav vienāds ar y")
else:
    print("x ir vienāds ar y")

# vai ar ==

if x == y:
    print("x ir vienāds ar y")
else:
    print("x nav vienāds ar y")    

# vēl viens operators and


punkti = int(input("Punkti: "))

if punkti >= 90 and punkti <= 100:
    print("Vērtējums: 10")
elif punkti >=80 and punkti < 90:
    print("Vērtējums:9")
elif punkti >=70 and punkti < 80:
    print("Vērtējums: 8")
elif punkti >=60 and punkti < 70:
    print("Vērtējums: 7")
else:
    print("Vērtējums: n/v")

# nav slikti, darbojas pareizi
# vai varam paaugstināt tā lasāmību?
# kodolīgāk?

punkti = int(input("Punkti: "))

if 90 <= punkti <= 100:
    print("Vērtējums: 10")
elif 80 <= punkti < 90:
    print("Vērtējums:9")
elif 70 <= punkti < 80:
    print("vērtējums: 8")
elif 60 <= punkti < 70:
    print("Vērtējums: 7")
else:
    print("Vērtējums: n/v")

# vai vēl labāk?

punkti = int(input("Punkti: "))

if punkti >= 90:
    print("Vērtējums: 10")
elif punkti >=80:
    print("Vērtējums:9")
elif punkti >= 70:
    print("Vērtējums: 8")
elif punkti >= 60:
    print("Vērtējums: 7")
else:
    print("Vērtējums: n/v")
    
    # https://video.cs50.io/_b6NgY_pMdw?start=387  34.min.
    # https://learning.edx.org/course/course-v1:HarvardX+CS50P+Python/block-v1:HarvardX+CS50P+Python+type@sequential+block@d25e27c90c304b0293d1f8dbda47c1b6/block-v1:HarvardX+CS50P+Python+type@vertical+block@298bd11c8ce4404b9d9b4bf12f4b1bf4