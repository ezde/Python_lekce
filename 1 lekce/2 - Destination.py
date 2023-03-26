osloveni = input("Jak ti máme říkat?")

print("Dobrý den",osloveni + ", vítá vás elektronický objednávkový systém")
ODELOVAC = 50 * "="
print(ODELOVAC)
print("""Nabízené destinace:
1 Praha     1000
2 Vídeň     1100
3 Brno      2000
4 Svitavy	1500
5 Zlín      2300
6 Ostrava   3400""")
#LIST - výběrová matice, uchovává více hodnot
mesto= ["Praha", "Vídeň", "Brno", "Svitavy", "Zlin", "Ostrava"]
mesta_se_slevou = ["Ostrava", "Vídeň"]
ceny= [1000, 1100, 2000, 1500, 2300, 3400]

#nastavení proměných
vyber = input("Vyber destinaci a zadej její číslo (1 až 6):")
if not vyber.isnumeric():
    print("Vybral jsi neplatnou hodnotu, musíš znovu", osloveni)
    exit()
if int(vyber) < 1 or int(vyber) > 6:
    print("Vybral jsi neplatnou hodnotu, musíš znovu", osloveni)
    exit()

mesto_vyber =str(mesto[int(vyber) -1])
cena_vyber = float(ceny[int(vyber) -1])
if mesto_vyber in mesta_se_slevou:
    cena_vyber= cena_vyber * 0.75
    #print(cena_vyber)

print(ODELOVAC)
print(osloveni, "jako cílovou stanici jsi vybral:"+ mesto_vyber, "Cena jízdenky:"+ str(cena_vyber)+"Kč")

print(ODELOVAC)
print(ODELOVAC)
jmeno = input("zadej svoje křestní jméno:")
if not jmeno.isalpha or len(jmeno)< 3:
    print("Do jména jsi vložil číslo, nebo délka jména je menší než 3 znaky, začni znovu")
    exit()
prijmeni = input("zadej svoje příjmení:")
if not prijmeni.isalpha or len(prijmeni)< 3:
    print("Do příjmení jsi vložil číslo, nebo délka příjmení je menší než 3 znaky, začni znovu")
    exit()
narozeni = input("zadej rok narození:")
if not int(narozeni.isnumeric()):
    print("Do roku narození zadéj pouze číslo")
    exit()
vek = 2020 - int(narozeni)
if not vek >= 18:
    print("není ti 18 let, nemůžeš si objednat")
    exit()
email = input("zadej svůj email:")
if not "@" in email or  not "." in email:
    print("špatně zadaný email")
    exit()
heslo = input("zadej heslo:")
if len(heslo) < 4:
    print("Heslo má málo znaků")
    exit()


print(ODELOVAC)
print(ODELOVAC)

print("Jméno:", jmeno)
print("Příjmení:",prijmeni)
print("Rok narození:", narozeni)
print("Emailová adresa:", email)
print("Heslo:", heslo)
print(ODELOVAC)

print("Díky za nákup")
