#!/usr/bin/python3
"""Lekce #11 - Uvod do programovani, importovani - pomocne"""

import os

# nacti soubory
def nacti_soubor(soubor: str)->list:
    try:
        with open(soubor, "r", encoding="utf-8") as txt:
            obsah = txt.readlines()

    except FileNotFoundError:
        print(f"TXT soubor: {soubor}, neexistuje")
    else:
        return obsah

    #print(f" Načítám: {soubor}")

# vytvor prazdny adresar
def vytvor_adresar(jmeno_sl: str)-> None:
    os.mkdir(jmeno_sl)


# vytvor jeden soubor
def vytvor_so(jmeno_so: str) -> None:
    if not os.path.isfile(jmeno_so):
        with open(jmeno_so, "w") as soub:
            print(f"Vytvarim: {jmeno_so}")
    else:
        print(f"Jméno soubotu {jmeno_so}, existuje")

def vytvor_vsechny_soubory(vsechna_jmena: list, jmeno_adresare: str)->None:
    for jmeno in vsechna_jmena:
        vytvor_so(os.path.join(os.path.abspath(jmeno_adresare), jmeno.strip()))
