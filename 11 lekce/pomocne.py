#def: nacteme vstupni soubor
import json
import csv
def nacti_json(soubor: str)-> dict:
    try:
        with open(soubor, "r") as cteni:
            obsah = json.load(cteni)

    except FileNotFoundError:
        print(f"soubour neexistuje {soubor}")

    else:
        return obsah

#def: zpracovani udaju
def zpracovavam_udaje(data: list) -> dict:
    upravene_udaje = {}
    for index, udaj in enumerate(data, 1):
        upravene_udaje[f"ID_{index}"] = {
            "jmeno": udaj["first_name"],
            "prijmeni": udaj["last_name"],
            "email": udaj["email"],
        }
    #print(f"Upravene: {upravene_udaje}")
    return upravene_udaje

#def: ulozit na vystupu
def ulozeni_udaju(slovnik: dict, soubor: str) -> None:
    with open(soubor, mode="w", newline="") as csv_soub:
        zahlavi= slovnik["ID_1"].keys()
        zapisovac = csv.DictWriter(csv_soub, fieldnames=zahlavi)

        zapisovac.writeheader()
        for zamestnanec in slovnik:
            zapisovac.writerow({
                "jmeno": slovnik[zamestnanec]["jmeno"],
                "prijmeni": slovnik[zamestnanec]["prijmeni"],
                "email": slovnik[zamestnanec]["email"],
            })

    print(f"Zapsano do: {soubor}.")