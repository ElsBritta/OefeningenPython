nummer_tombola = int(input())
e =nummer_tombola%10
t = (nummer_tombola//10)%10
h = (nummer_tombola//100)%10
d = nummer_tombola//1000
if h%3 ==0:
  print("Proficiat, je hebt een prijs gewonnen!")
elif 3>= e or e>= 8:
  print("Je krijgt nog een troostprijs.")  
else:
  print("Jammer, volgende keer meer geluk.")
