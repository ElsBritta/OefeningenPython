getal1 = float(input("Geef eerste getal:"))
getal2 = float(input("Geef tweede getal:"))
getal3 = float(input("Geef derde getal:"))

if getal1 > getal2 and getal1 < getal3:
  print(getal1)
elif getal2 > getal1 and getal2 < getal3:
  print(getal2)
else:
  print(getal3)  