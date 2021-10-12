def Tekening_Galg(fouten):
        if fouten == 1:
              print("""  
     |
     |
     |
     |
     |
_____|""")
        elif fouten == 2:
           print("""  ____
     |
     |
     |
     |
     |
_____|""")
        elif fouten == 3:
            print("""  ____
    \|
     |
     |
     |
     |
_____|""")
        elif fouten == 4:
              print("""  ____
  | \|
     |
     |
     |
     |
_____|""")
        elif fouten == 5:
              print("""  ____
  | \|
  0  |
     |
     |
     |
_____|""")
        elif fouten == 6:
              print("""  ____
  | \|
  0  |
  |  |
     |
     |
_____|""")
        elif fouten == 7:
              print("""  ____
  | \|
  0  |
 -|  |
     |
     |
_____|""")
        elif fouten == 8:
              print("""  ____
  | \|
  0  |
 -|- |
     |
     |
_____|""")
        elif fouten == 9:
              print("""  ____
  | \|
  0  |
 -|- |
 /   |
     |
_____|""")
        elif fouten ==10:
              print("Helaas, je bent dood")
              print("""  ____
  | \|
  0  |
 -|- |
 / \ |
     |
_____|""")

def Kieswoord():
  import random
  compwoordenlijst = ["omdat", "elkaar", "altijd", "terwijl", "niemand", "iemand", "antwoord", 
  "voorbij", "kasteel", "aantal", "vandaag", "daarmee", "leeftijd", "voordat", "eenmaal", 
  "langzaam", "omhoog", "hoewel", "ervan", "waarvan", "soldaat", "vandaan", "daarvan", "waarmee", 
  "waardoor", "totdat", "hoeveel", "eiland", "voorschijn", "daarbij", "daarvoor", "sultan", 
  "voeding", "erbij", "koopman", "daardoor", "ervoor", "waarheid", "ermee", "waarbij",
  "afscheid", "persoon", "schoonheid", "oorlog", "voorbeeld", "rijkdom", "handboek", 
  "opdat", "inhoud", "normaal", "dienaar", "doordat", "maaltijd", "indien", "voorhoofd", 
  "wijsheid", "ontdekt", "aldus", "houding", "daarnaast"]    
  return random.choice(compwoordenlijst)

def Vervang(gokje,LengteWoord, TeRadenWoord,temp):
  for i in range(0, LengteWoord):
    if gokje == TeRadenWoord[i]:
      temp = temp[:i] + gokje +temp[i+1:]
  return temp
	
    	
