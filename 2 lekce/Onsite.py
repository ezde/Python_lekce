film1 = {
    'JMENO': 'Shawshank Redemption',
    'HODNOCENI': "93/100",
    'ROK': 1994,
    'REZISER': 'Frank Darabont',
    'STOPAZ': 144,
    'HRAJI': (
        "Tim Robbins",
        "Morgan Freeman",
        "Bob Gunton",
        "William Sadler",
        "Clancy Brown",
        "Gil Bellows",
        "Mark Rolston",
        "James Whitmore",
        "Jeffrey DeMunn",
        "Larry Brandenburg"
    ),
}

film2 = {
    "JMENO": "The Godfather",
    "HODNOCENI": "92/100",
    "ROK": 1972,
    "REZISER": "Francis Ford Coppola",
    "STOPAZ": 175,
    "HRAJI": (
        "Marlon Brando",
        "Al Pacino",
        "James Caan",
        "Richard S. Castellano",
        "Robert Duvall",
        "Sterling Hayden",
        "John Marley",
        "Richard Conte"
    ),
}

film3 = {
    "JMENO": "The Dark Knight",
    "HODNOCENI": "90/100",
    "ROK": 2008,
    "REZISER": "Christopher Nolan",
    "STOPAZ": 152,
    "HRAJI": (
        "Christian Bale",
        "Heath Ledger",
        "Aaron Eckhart",
        "Michael Caine",
        "Maggie Gyllenhaal",
        "Gary Oldman",
        "Morgan Freeman",
        "Monique Gabriela",
        "Ron Dean",
        "Cillian Murphy"
    ),
}

film4 = {
    "JMENO": "The Prestige",
    "HODNOCENI": "85/100",
    "ROK": 2006,
    "REZISER": "Christopher Nolan",
    "STOPAZ": 130,
    "HRAJI": (
        "Hugh Jackman",
        "Christian Bale",
        "Michael Caine",
        "Piper Perabo",
        "Rebecca Hall",
        "Scarlett Johansson",
        "Samantha Mahurin",
        "David Bowie"
    )
}

#filmový slovník
from pprint import pprint
filmovy_slovnik = {}
oddelovac="="*76

filmovy_slovnik[film1["JMENO"]]= film1
filmovy_slovnik[film2["JMENO"]]= film2
filmovy_slovnik[film3["JMENO"]]= film3
filmovy_slovnik[film4["JMENO"]]= film4
#pprint(filmovy_slovnik)


print(oddelovac)
#pokud chci formátovat text, když nevím mohu použít funkci help(str)
print("Vitejte v nasi skromne filmove databazi".center(76, " "))
#mohu použít f-print - nová funkce, kde nemusím se zabívat, zda je to int, str, + nebo , . proměnou rovnou vložím do složené závorky
print(f"""{oddelovac}
Vyberte kategorii:
{oddelovac}
{"VSECHNY FILMY | DETAILY FILMU | SPOLECNI HERCI | VSICHNI REZISERI".center(76, " ")}
{oddelovac}
 """)

vyber=input("Vyberte možnost: ").lower()
if vyber == "vsechny filmy":
    print(oddelovac)
    print("všechny naše filmy".center(76, " "))
    print(oddelovac)
    #pohledy
    print(list(filmovy_slovnik.keys()))
elif vyber == "detaily filmu":
    print(oddelovac)
    print(list(filmovy_slovnik.keys()))
    print(oddelovac)
    vyber_film=input("napiš název filmu: ")
    print(oddelovac)
    print("Detail k vybranému filmu".center(76, " "))
    pprint(filmovy_slovnik.get(vyber_film, "název filmu není správně nebo není v databázi"))
elif vyber=="spolecni herci":
    print(oddelovac)
    print(list(filmovy_slovnik.keys()))
    print(oddelovac)
    vyber_film1 = input("napiš název prvního filmu: ")
# moznosti zapisu
# set1 = set(filmovy_slovnik[vyber_film1].get("HRAJI", "tento film nemáme v nabídce, nebo je špatně napsaný")
    set1= set(filmovy_slovnik[vyber_film1]["HRAJI"])
    vyber_film2 = input("napiš název druhého filmu: ")
    set2=set(filmovy_slovnik[vyber_film2]["HRAJI"])
    print(oddelovac)
    if len(set1 & set2)!= 0:
        print("Společní herci: ".center(76, " "))
        print(set1 & set2)
    else:
        print("tyto dva filmy nemají společné herce")
elif vyber=="vsichni reziseri":
    reziser =(
        filmovy_slovnik["The Prestige"]["REZISER"],
        filmovy_slovnik["The Dark Knight"]["REZISER"],
        filmovy_slovnik["The Godfather"]["REZISER"],
        filmovy_slovnik['Shawshank Redemption']["REZISER"]
        )
    print(f"{set(reziser)}")
