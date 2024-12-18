import os 
os.system('cls') # attīra termināla logu pašā sākumā
print("\n")  # ieliek tukšu rindiņu pirms izdrukas 

# def main():
#     dollars = dollars_to_float(input("How much was the meal? "))
#     percent = percent_to_float(input("What percentage would you like to tip? "))
#     tip = dollars * percent
#     print(f"Leave EUR {tip:.2f}")


# def dollars_to_float(d):
#     d_bez_eur = d.replace("EUR", "")
#     return float(d_bez_eur)


# def percent_to_float(p):
#     p_bez_proc = p.replace("%", "")
#     p_converted = float(p_bez_proc) / 100
#     return p_converted


# main()




def main():
    nauda, valutas_nosaukums = nauda_to_float(input("Cik jāmaksā par pasūtījumu? "))
    procenti = procenti_to_float(input("Cik procentus atstāsim dzeramnaudai? "))
    tip = nauda * procenti
    print(f"Jāatstāj  {tip:.2f} {valutas_nosaukums}")


def nauda_to_float(d):
    import re
    nauda_bez_valutas = re.search(r'\d+', d)
    d_bez_eur = int(nauda_bez_valutas.group())
    valutas_nosaukums = d.replace(nauda_bez_valutas.group(), "").strip().upper()
    return float(d_bez_eur), valutas_nosaukums


def procenti_to_float(p):
    p_bez_proc = p.replace("%", "")
    p_converted = float(p_bez_proc) / 100
    return p_converted


main()
