nummer_tombola = int(input())
e =nummer_tombola%10
t = (nummer_tombola//10)%10
d = nummer_tombola//1000
if t%2 ==0:
  print("Proficiat, je hebt een prijs gewonnen!")
elif 4<= d <=6:
  print("Je krijgt nog een troostprijs.")  
else:
  print("Jammer, volgende keer meer geluk.")  