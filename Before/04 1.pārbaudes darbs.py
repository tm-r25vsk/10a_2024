# 1. uzdevums. Paroles pārbaude
# Lietotājam tiek prasīts ievadīt paroli. Izveido programmu, kas pārbauda, vai parole atbilst šādiem nosacījumiem:
#      - Parolei jābūt vismaz 9 simbolu garai.
#      - Parolei jāsatur vismaz viens lielais burts.
#      - Parolei jāsatur vismaz viens cipars.
# **Ieteikumi**
# var izmantot `if` nosacījumus ar virknes metodēm, piemēram, `isupper()`, `isdigit()`, un `len()`.
# **Piemērs**
#      - Ievade: `Python123`
#      - Izvade: `Parole atbilst visiem nosacījumiem!`

# Ievades pieprasīšana no lietotāja
parole = input("Ievadi paroli: ")

# Pārbaudes nosacījumi
if len(parole) >= 9:
    if any(char.isupper() for char in parole):
        if any(char.isdigit() for char in parole):
            print("Parole atbilst visiem nosacījumiem!")
        else:
            print("Parolei jāsatur vismaz viens cipars.")
    else:
        print("Parolei jāsatur vismaz viens lielais burts.")
else:
    print("Parolei jābūt vismaz 9 simbolu garai.")

# ================================================================

# 2.uzdevums. Garais/īsais gads/gadsimts
# Lietotājs ievada gadu (piemēram, 1999). Programma nosaka, kurā gadsimtā tas ir un vai tas ir garais vai īsais gads.
#      - Garie gadi ir tie, kuri ir dalāmi ar 400 vai dalāmi ar 4, bet ne ar 100.
#      - Gadsimts ir skaitlis, kas tiek iegūts, dalot gadu ar 100 un noapaļojot uz augšu.
# **Ieteikumi**
# var izmantot `if` nosacījumus un dalījuma (`//`) operatoru.
# **Piemērs**
#      - Ievade: `1900`
#      - Izvade: `20. gadsimts, īsais gads`


# Ievades pieprasīšana no lietotāja
gads = int(input("Ievadi gadu: "))

# Gadsimta aprēķins, noapaļojot uz augšu
gadsimts = (gads + 99) // 100

# Nosaka, vai gads ir garais vai īsais
if (gads % 400 == 0) or (gads % 4 == 0 and gads % 100 != 0):
    garais_gads = True
else:
    garais_gads = False

# Rezultāta izvadīšana
if garais_gads:
    print(f"{gadsimts}. gadsimts, garais gads")
else:
    print(f"{gadsimts}. gadsimts, īsais gads")

# ================================================================

# 3.uzdevums. Vecuma un biļešu cenas aprēķins
# Lietotājam tiek prasīts ievadīt vecumu. Programma izvada biļetes cenu, pamatojoties uz šādiem nosacījumiem:
#      - Ja vecums ir mazāks par 7 gadiem, biļete ir bez maksas.
#      - Ja vecums ir no 7 līdz 18 gadiem, biļete maksā 5 eiro.
#      - Ja vecums ir no 18 līdz 65 gadiem, biļete maksā 10 eiro.
#      - Ja vecums ir virs 65 gadiem, biļete maksā 3 eiro.
# **Ieteikumi**
# var izmantot vairākus `if`, `elif` un `else` nosacījumus.
# **Piemērs**
#      - Ievade: `70`
#      - Izvade: `Biļetes cena ir 3 eiro.`

# Ievades pieprasīšana no lietotāja
vecums = int(input("Ievadi savu vecumu: "))

# Nosaka biļetes cenu, izmantojot nosacījumus
if vecums < 7:
    cena = 0
elif 7 <= vecums <= 18:
    cena = 5
elif 18 < vecums <= 65:
    cena = 10
else:
    cena = 3

# Izvada biļetes cenu
print(f"Biļetes cena ir {cena} eiro.")

# ================================================================

# 4.uzdevums. Skaitļa kategorija
# Lietotājam tiek prasīts ievadīt skaitli. Programmai jāizvada, kurai kategorijai šis skaitlis pieder:
#      - Ja skaitlis ir negatīvs, izdrukā “Negatīvs skaitlis”.
#      - Ja skaitlis ir nulle, izdrukā “Nulle”.
#      - Ja skaitlis ir pozitīvs, izdrukā “Pozitīvs skaitlis”.
#      - Papildus pārbaudi, vai skaitlis ir pāra vai nepāra.
# **Ieteikumi**
# Izmanto `if` un `elif`, kā arī `mod` operatoru (`%`), lai pārbaudītu, vai skaitlis ir pāra vai nepāra.
# **Piemērs**
#      - Ievade: `-5`
#      - Izvade: `Negatīvs skaitlis. Nepāra skaitlis.`

# Ievades pieprasīšana no lietotāja
skaitlis = int(input("Ievadi veselu skaitli: "))

# Pārbaude, vai skaitlis ir negatīvs, nulle vai pozitīvs
if skaitlis < 0:
    print("Negatīvs skaitlis.")
elif skaitlis == 0:
    print("Nulle.")
else:
    print("Pozitīvs skaitlis.")

# Pārbaude, vai skaitlis ir pāra vai nepāra
if skaitlis % 2 == 0:
    print("Pāra skaitlis.")
else:
    print("Nepāra skaitlis.")

