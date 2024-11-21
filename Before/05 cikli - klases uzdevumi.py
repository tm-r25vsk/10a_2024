# 1. Perfekti skaitļi
# Uzraksti programmu, kas atrod visus perfektos skaitļus diapazonā no 1 līdz 10,000. Perfekts skaitlis ir tāds, kura dalītāju summa (izņemot pašu skaitli) ir vienāda ar pašu skaitli. Piemēram, 6 ir perfekts, jo 
# 1 + 2 + 3 = 6


for n in range(1, 10001):
    dalitaju_summa = 0
    for i in range(1, n):
        if n % i == 0:
            dalitaju_summa += i
    if dalitaju_summa == n:
        print(f"{n} ir perfekts skaitlis.")
        
        
# 2. Skaitļu piramīda
# Izveido programmu, kas ar while ciklu ģenerē skaitļu piramīdu līdz konkrētam skaitlim 
# n, kuru ievada lietotājs. 

# Piemēram, ja n=5, 
# izvada: 
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

n = int(input("Ievadiet skaitli: "))
rinda = 1
while rinda <= n:
    for i in range(1, rinda + 1):
        print(i, end=" ")
    print()
    rinda += 1

# 3. Fibonacci virkne
# Uzraksti programmu, kas ar while ciklu ģenerē pirmos 15 Fibonacci virknes skaitļus. Fibonacci virkne sākas ar 0 un 1, un katrs nākamais skaitlis ir iepriekšējo divu summa.

f1, f2 = 0, 1
count = 0
while count < 15:
    print(f1, end=" ")
    f1, f2 = f2, f1 + f2
    count += 1

# 4. Pirmskaitļi
# Izveido programmu, kas ar for ciklu izvada visus pirmskaitļus no 1 līdz 100.


for num in range(2, 101):
    ir_pirmais = True
    for dalitajs in range(2, int(num ** 0.5) + 1):
        if num % dalitajs == 0:
            ir_pirmais = False
            break
    if ir_pirmais:
        print(num, end=" ")
        
        
# 5. Spoguļskaitļi
# Uzraksti programmu, kas atrod visus skaitļus diapazonā no 10 līdz 1000, kuri ir vienādi, ja tos nolasa no abiem galiem (piemēram, 121, 242).


for num in range(10, 1000):
    if str(num) == str(num)[::-1]:
        print(num, end=" ")
        
# 6. Skaitļu spēle
# Izveido programmu, kas ļauj datoram uzminēt skaitli, kuru izvēlas lietotājs diapazonā no 1 līdz 100. Lietotājs sniedz atbildes "mazāk", "vairāk" vai "pareizi".


print("Iedomājies skaitli no 1 līdz 100, un dators mēģinās to uzminēt!")
min_robeza = 1
max_robeza = 100
atbilde = ""

while atbilde != "pareizi":
    minejums = (min_robeza + max_robeza) // 2
    print(f"Dators saka: Vai jūsu skaitlis ir {minejums}?")
    atbilde = input("Atbildiet ar 'mazāk', 'vairāk' vai 'pareizi': ").strip().lower()
    if atbilde == "mazāk":
        max_robeza = minejums - 1
    elif atbilde == "vairāk":
        min_robeza = minejums + 1

print("Dators uzminēja jūsu skaitli!")

# 7. Skaitļu secība ar noteikumu
# Uzraksti programmu, kas izvada skaitļus no 1 līdz 50, izņemot tos, kas dalās ar 3 vai 5.


for num in range(1, 51):
    if num % 3 != 0 and num % 5 != 0:
        print(num, end=" ")


# 8.Dzīves ceļa skaitlis
# Ezoteriskajā skatījumā cilvēka dvēsele pati izvēlas laiku, kurā nākt uz Zemes, un tas sevī ietver informāciju gan par iepriekšējo dzīvju pieredzi, gan konkrētā iemiesojuma scenāriju, no kura vēl neviens nav izbēdzis. 
# Dzimšanas gads, mēnesis un datums, saskaitot tos visus kopā, veido tā saukto dzīves ceļa skaitli, kurš norāda virzienu, kas ejams, lai piepildītu savu misiju, palīdz saprast, ar ko būtu jānodarbojas.


# Dzīves ceļa skaitlis ir viens no būtiskākajiem skaitļiem numeroloģijā. Dzīves ceļa skaitlis parāda kādas rakstura īpašības un talanti Jums ielikti šūpulī un kādi ir Jūsu dzīves mērķi un misija.

# Dzīves ceļa skaitli iegūst saskaitot visus dzimšanas datuma skaitļus (piemēram 14.10.1980 būtu 1+4+1+0+1+9+8+0=24=2+4=6) un noreducējot līdz 1, izņemot gadījumus, kad sanāk 11, 22 vai 33, kas ir meistara skaitļi. 
# (https://tarokartis.lv/dzives-cela-skaitlis-numerologija/)

# Uzrakstīt programmu, kas aprēķina dzīves ceļa skaitli.

# Piemēram, ja dzimšanas datums ir 1999. gada 12. novembris, skaitļu valodā tas izskatīsies šādi: 1999.12.11. Lai iegūtu dzīves skaitli, jāsaskaita 1+9+9+9+1+2+1+1=33, pēc tam summa jāsaskaita, lai iegūtu viencipara skaitli, tātad 3+3=6, līdz ar to esam ieguvuši dzīves ceļa skaitli 6.


# Lietotāja dzimšanas datuma ievade
print("Ievadiet savu dzimšanas datumu:")
gads = int(input("Gads (piem., 1987): "))
menesis = int(input("Mēnesis (1-12): "))
datums = int(input("Datums (1-31): "))

# Saskaitām dzimšanas datuma ciparus
dzimsanas_summa = sum(int(cipars) for cipars in f"{gads}{menesis:02}{datums:02}")

# Samazinām līdz viencipara skaitlim vai meistarskaitlim
while dzimsanas_summa > 9 and dzimsanas_summa not in {11, 22, 33}:
    dzimsanas_summa = sum(int(cipars) for cipars in str(dzimsanas_summa))

# Rezultāta izvadīšana
print(f"Jūsu dzīves ceļa skaitlis ir: {dzimsanas_summa}")

