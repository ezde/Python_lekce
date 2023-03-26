#importovani
import sys
from pomocne import nacti_json
from pomocne import zpracovavam_udaje
from pomocne import ulozeni_udaju

#hlavni funkce --> rozdelit povinost
def hlavni()-> None:
    if sys.argv[1] == "do-csv":
        nacteny_json = nacti_json("ORIG.json")
        #print(f"Nacteny json: {nacteny_json}")
        zpracovane = zpracovavam_udaje(nacteny_json)
        ulozeni_udaju(zpracovane, "vystupni_csv.csv")

    else:
       print (f"neplatný argument:")

hlavni()