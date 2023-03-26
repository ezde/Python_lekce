KOSIK = {}
ODDELOVAC = "=" * 40
POTRAVINY = {
    "mleko": [30, 5],
    "maso": [100, 1],
    "banan": [30, 10],
    "jogurt": [10, 5],
    "chleb": [20, 5],
    "jablko": [10, 10],
    "pomeranc": [15, 10]
}

from pprint import pprint

print(ODDELOVAC)
print("VITEJTE V NASEM VIRTUALNIM OBCHODE!", end=f"\n{ODDELOVAC}\n")
print("VYBERTE SI Z NASEHO ZBOZI:", end=f"\n{ODDELOVAC}\n")
tabulka = POTRAVINY.copy()
while tabulka:
    radek_potravina= tabulka.popitem()
    print(f"POTRAVINA: {radek_potravina[0]},\tCENA: {radek_potravina[1][0]}")
#pprint(POTRAVINY)
print(ODDELOVAC)

#zadání potraviny přes input
#prepinac = True


#while prepinac:
while (vyber_potravinu:=input("co chceš koupit?: ")) != "q":
    #vyber_potravinu= input("co chceš koupit?: ")
    if vyber_potravinu == "q":
        prepinac= False
   # elif vyber_potravinu not in POTRAVINY:
        #print(f"*{vyber_potravinu}* NEMAME SKLADEM!")
    else:
        KOSIK[vyber_potravinu] = POTRAVINY[vyber_potravinu][0]
else:
    print(ODDELOVAC)
    print("Nákup jsi ukončil", end=f"\n{ODDELOVAC}\n")
    print(KOSIK, end=f"\n{ODDELOVAC}\n")
    print(f"CENA CELKEM: {sum(KOSIK.values())} CZK", end=f"\n{ODDELOVAC}\n")

