# Latvijas transportlīdzekļu numura zīmes jeb valsts reģistrācijas numura zīmes ir Latvijas teritorijā Ceļu satiksmes drošības direkcijas (CSDD) reģistrēto transportlīdzekļa numura zīmes, kas tiek piestiprinātas to aizmugurē un priekšpusē (automašīnām). Vispārējās izmantošanas numura zīmes ir melnā krāsā uz balta fona.
# Numura zīmēs ir divi latīņu alfabēta burti (izņemot Q, W, Y) un no viena līdz četriem cipariem, kas veido skaitļus no 1 līdz 9999. Starp burtiem un skaitli ir domu zīme
# Jāuzraksta programma python, kas pārliecinās vai ievadītais numurs atbilst noteikumiem.



import re

# Lietotāja ievade
numurs = input("Ievadiet transportlīdzekļa numura zīmi: ").strip().upper()

# Regulārās izteiksmes modelis Latvijas numura zīmēm
modelis = r"^[A-PR-UZ]{2}-[1-9]\d{0,3}$"

# Pārbaude un rezultāts
if re.match(modelis, numurs):
    print(numurs," numura zīme ir derīga.")
else:
    print(numurs," numura zīme nav derīga.")




# Regulārās izteiksmes modelis (modelis):

# ^[A-PR-UZ]{2}: Pirmajā daļā jābūt diviem burtiem no latīņu alfabēta (izņemot Q, W, Y).
# -: Pēc burtiem ir domu zīme.
# [1-9]\d{0,3}$: Skaitlim jābūt no 1 līdz 9999 (pirmais cipars nevar būt 0).
# re.match:

# Funkcija pārbauda, vai ievadītais teksts atbilst definētajam modelim.
# Ievades apstrāde:

# input saņem numura zīmi no lietotāja.
# .strip() noņem liekās atstarpes.
# Rezultāts:

# Ja numura zīme atbilst modelim, tiek izvadīts, ka tā ir derīga.
# Pretējā gadījumā tiek ziņots, ka numura zīme nav derīga.

# vai arī

# Lietotāja ievade
ievade = input("Ievadiet transportlīdzekļu numura zīmes, atdalot tās ar komatiem: ").strip().upper()

# Saraksta izveidošana no ievades
numuri = ievade.split(',')

# Pārlasīt katru numura zīmi ar for ciklu
for numurs in numuri:
    numurs = numurs.strip()  # Noņemt liekās atstarpes

    # Pārbaudīt garumu un struktūru
    if len(numurs) < 4 or '-' not in numurs:
        print(f"{numurs}: Numura zīme nav derīga.")
        continue

    burti, cipari = numurs.split('-')

    # Pārbaudīt, vai burti ir divi un derīgi
    if len(burti) != 2 or not all(burts.isalpha() and burts in "ABCDEFGHIJKLMNOPRSTUVZ" for burts in burti.upper()):
        print(f"{numurs}: Numura zīme nav derīga.")
        continue

    # Pārbaudīt, vai cipari ir skaitlis no 1 līdz 9999
    if not cipari.isdigit() or not (1 <= int(cipari) <= 9999):
        print(f"{numurs}: Numura zīme nav derīga.")
        continue

    # Ja viss der
    print(f"{numurs}: Numura zīme ir derīga.")
 
#  Sadalīšana sarakstā:

# Lietotājs ievada numura zīmes, atdalot tās ar komatiem.
# Programma sadala ievadīto tekstu sarakstā, izmantojot .split(',').
# Loģiskā pārbaude:

# Pārbauda garumu un struktūru:
# Numura zīmei jābūt vismaz 4 rakstzīmēm un jāietver domu zīme (-).
# Burti:
# Jābūt tieši diviem burtiem, kas pieder pie atļautā alfabēta ("ABCDEFGHIJKLMNOPRSTUVZ").
# Cipari:
# Pārbauda, vai cipari ir derīgi skaitļi no 1 līdz 9999.
# Rezultāti:

# Tiek izvadīts, vai katra ievadītā numura zīme ir derīga vai nē.