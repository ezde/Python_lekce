import requests
import sys
import csv
from bs4 import BeautifulSoup


# http://heroes3.cz/hraci/index.php?page=2&order=&razeni=DESC
# hlavní fce -> main()
def hlavni() -> None:
    if "http://heroes3.cz/hraci/index.php?page=" in sys.argv[1] and ".csv" in sys.argv[2]:
        odkaz: str = sys.argv[1]
        soubor = sys.argv[2]
        print(f"Odkaz: {odkaz}")
        raw_html = ziskej_odpoved(odkaz)
        bs4_text = parsuj_raw_html(raw_html)
        # print(bs4_text)
        vsechny_radky = hledej_hrace(bs4_text)

        udaje = [zpracuj_udaje(radek) for radek in vsechny_radky if vsechny_radky]
        print(f"ULOZENO DO:{soubor}") if uloz_csv(soubor, udaje) else print("CHYBA")
    else:
        print(f"Není zadáno správně")


# odeslat požadavek na server
def ziskej_odpoved(url: str) -> None:
    with requests.Session() as req:
        return req.get(url).text  # získávám raw html
    # print(f"Získávám odpověď:")


# Parsovat odpoved servu pro nase potreby
def parsuj_raw_html(html: str) -> BeautifulSoup:
    return BeautifulSoup(html, "html.parser")

    # print(f"Parsuji....")


# Najít informace o hracich
def hledej_hrace(html: BeautifulSoup) -> list:
    table = html.find("table", {"class": "tab_top"})
    return table.find_all("tr")[1:]

    # print(f"Upraveno: {table}")


def zpracuj_udaje(tr: str) -> dict:
    return {
        "poradi": tr.find_all("td")[0].text,
        "jmeno": tr.find_all("td")[2].text,
        "body": tr.find_all("td")[3].text,
        "celkem": tr.find_all("td")[6].text,
        "vitezstvi": tr.find_all("td")[5].text,
        "uspesnost": tr.find_all("td")[7].text,
    }


# ukladame .csv soubor
def uloz_csv(jmeno: str, data: list) -> None:
    with open(jmeno, mode="w", newline="") as csv_v:
        zahlavi = data[0].keys()
        zapisovac = csv.DictWriter(csv_v, delimiter=",", fieldnames=zahlavi)
        zapisovac.writeheader()
        for index, _ in enumerate(data):
            zapisovac.writerow({
                "poradi": data[index]["poradi"],
                "jmeno": data[index]["jmeno"],
                "body": data[index]["body"],
                "celkem": data[index]["celkem"],
                "vitezstvi": data[index]["vitezstvi"],
                "uspesnost": data[index]["uspesnost"],
            })
        return True


if __name__ == "__main__":
    hlavni()
