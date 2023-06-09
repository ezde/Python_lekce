#!/usr/bin/python3
"""Lekce #11 - Uvod do programovani, importovani - hlavni"""
import os
import sys

from pomocne import nacti_soubor, vytvor_soubor, vytvor_adresar



def hlavni() -> None:
    jmena = nacti_soubor(txt_soubor)
    if os.path.isdir(cil_adresar):
        print(f"SLOZKA: {cil_adresar} EXISTUJE!")

    else:
        vytvor_adresar(cil_adresar)

    for jmeno in jmena:
        vytvor_soubor(jmeno.strip(), os.path.join(os.getcwd(), cil_adresar))


if __name__ == "__main__":
    if len(sys.argv) == 3:
        txt_soubor = sys.argv[1]
        cil_adresar = sys.argv[2]
        hlavni()
    else:
        print("INCORRECT USAGE: python <file>.py <txt_file> <dir>")
