pravda = True
nepravda = False
print(type(pravda))

#Podmínky
vek= int(input("Kolik je ti let:"))
if vek >= 18:
    print("Tady máš škopek")
elif vek == 17:
    print("kamarade fakt smůla, ale ještě nemůžeš")
else:
    print("Utíkej, nebo zavolám mamince")

nakupni_seznam=["Chleba", "Mouka", ]
if "Chleba" in nakupni_seznam:
    print("Chleba máme")
else:
    print("Chleba není")


