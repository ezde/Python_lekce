def hlavni() -> None:
    nactena_cisla = nacitani_udaju("C:\Programování\python-academy\pátá lekce\cisla.txt")
    vysledna_cisla = preved_udaje(nactena_cisla)
    return vysledna_cisla
    # print(f"Cisla: {vysledna_cisla}")


# otevrit soubor

def nacitani_udaju(path: str, rezim: str = "r") -> list:
    with open(path, rezim) as txt:
        return txt.readlines()


def preved_udaje(data: list) -> list:
    ciselne_udaje = []
    for udaj in data:
        try:
            cislo = int(udaj)

        except ValueError:
            print(f"Nelze převést: {udaj}")
        else:
            print(f"Zapsané číslo: {cislo}")
            ciselne_udaje.append(cislo)
        finally:
            print("_"*40)

    return ciselne_udaje


hlavni()
