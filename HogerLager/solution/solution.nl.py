import random
getal1 = random.randint(1,13)
print(getal1)
aantal_juist = 0

for i in range(7):
    raden =input("Is het volgende getal hoger (h) of lager (l) ?")
    getal2= random.randint(1,13)
    if getal2 > getal1 and raden ==  "h":
        print("juist geraden")
        aantal_juist +=1
    elif getal2 < getal1 and raden == "l":
        print("juist geraden")
        aantal_juist +=1
    else:
        print("fout geraden")
    print(getal2)
    getal1 = getal2
print("Je hebt", aantal_juist, "keer goed geraden en", 7- aantal_juist,"keer fout geraden.")
