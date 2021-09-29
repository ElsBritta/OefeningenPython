import random
getal1 = random.randint(1,20)

gevonden = False
aantal  = 0

while aantal < 6 and not gevonden:
  x =int(input("Geef een getal"))
    
  if x==getal1:
    gevonden = True
  elif x < getal1 :
    print("Het te zoeken getal is groter")
  else:
    print("Het te zoeken getal is kleiner")
  aantal +=1
    
if gevonden:
  print("proficiat, je bent gewonnen")
else:
  print("Je hebt verloren.")

