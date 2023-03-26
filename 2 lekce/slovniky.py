
novy_slovnik1={}
print(type(novy_slovnik1))

novy_slovnik2=dict()
print(type(novy_slovnik2))


slovnik["jmeno"]="Zdenek"
slovnik["příjmení"]="Dvořák"

#funkce pro lepší print
from pprint import  pprint

pprint(film1)
print(rozdel)


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

rozdel="="*50


print(film1)

film1["JMENO"] = "Shawshank Redemption"
film1["HODNOCENI"] = "93/100"
film1["ROK"] = 1994
film1["REZISER"] = "Frank Darabont"
film1["STOPAZ"] = 144
film1["HRAJI"] = (
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
)

#funkce pro lepší print
from pprint import  pprint

pprint(film1)
print(rozdel)

# update slovníku
film1.update({"JMENO": "XXXX"})
pprint(film1)
print(rozdel)
# vymazání ze slovníku pomocí del
del film1["JMENO"]
pprint(film1)
print(rozdel)

# vymazání ze slovníku pomocí .pop
film1.pop("REZISER")
pprint(film1)
print(rozdel)

# znovu vložení smazaného slovníku
film1["JMENO"] = "Shawshank Redemption"
film1["REZISER"] = "Frank Darabont"
pprint(film1)
print(rozdel)

#vložení seznamu do slovníku = nestovaní

