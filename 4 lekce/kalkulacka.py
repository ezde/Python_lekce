from pprint import pprint

ODDELOVAC = 100 * "="
OPTION = ["+", "-", "*", "/", "**", "prumer"]


# definition
def main():
    while True:
        welcome()
        display_ops()
        options = select_opt()
        if options not in OPTION:
            print("Toto je nepovolená funkce")
            continue

        if options == "+":
            selected_numbers = select_num(options)
            vypocet = add(selected_numbers[0], selected_numbers[1])
        elif options == "-":
            selected_numbers = select_num(options)
            vypocet = minus(selected_numbers[0], selected_numbers[1])
        elif options == "*":
            selected_numbers = select_num(options)
            vypocet = krat(selected_numbers[0], selected_numbers[1])
        elif options == "/":
            selected_numbers = select_num(options)
            vypocet = delen(selected_numbers[0], selected_numbers[1])
        elif options == "**":
            selected_numbers = select_num(options)
            vypocet = mocnina(selected_numbers[0], selected_numbers[1])
        elif options == "prumer":
            selected_numbers = select_num(options)
            print(selected_numbers)
            vypocet = prumer(selected_numbers)

        print(f"""Výsledek je: {vypocet}""")


def welcome():
    print(f"""
    {ODDELOVAC.center(100)}
    {"Ahoj uživateli, jsem program KALKULÁTOR a pomohu ti spočítat, co si budeš přát.".center(100)}
    {ODDELOVAC.center(100)}""")


def display_ops():
    print(f"""{" | ".join(OPTION).center(100)}
    {ODDELOVAC.center(100)}""")


def select_opt():
    result = input("Choice one options:".rjust(10))
    print(ODDELOVAC.center(100))
    print(ODDELOVAC)
    return result


def select_num(options):
    if options == "**":
        num1 = int(input("vlož první číslo:"))
        num2 = int(input("vlož mocnitele:"))
        return num1, num2


    elif options == "prumer":
        input_list = input("Zadej libovolnáý počet číslic a každé z nich odděl čárkou:").split(",")
        number_list = []
        for i in input_list:
            number_list.append(int(i))
        return number_list

    elif options in ["+", "-", "*", "/"]:
        num1 = int(input("vlož první číslo:"))
        num2 = int(input("vlož druhé číslo:"))
        return num1, num2


def add(a, b):
    return a + b


def minus(a, b):
    return a - b


def krat(a, b):
    return a * b


def delen(a, b):
    return a / b


def mocnina(numb, mocn):
    return numb ** mocn


def prumer(colection):
    return sum(colection) / len(colection)


main()
