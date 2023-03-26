#!/usr/bin/python3
"""Lekce #11 - Uvod do programovani, importovani - hlavni"""
from pomocne import nacti_soubor, vytvor_adresar, vytvor_so, vytvor_vsechny_soubory
import os
import sys

# vytvor hlavní ()

def hlavni() -> None:
    # volám fci pro nacitani souboru
    jmena = nacti_soubor(jmena_souboru)

    if not os.path.isdir(jmeno_adresare):
        vytvor_adresar(jmeno_adresare)
        vytvor_vsechny_soubory(jmena, jmeno_adresare)
    else:
        print(f"Složka adresáře {jmeno_adresare} existuje")
        vytvor_vsechny_soubory(jmena, jmeno_adresare)

if len(sys.argv) !=3:
    print("Jak pouzivat: hlavni.py jméno souboru jméno složky")
else:
    jmena_souboru = sys.argv[1]
    jmeno_adresare = sys.argv[2]
    hlavni()
