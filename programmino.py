somma = 0
num = 1

while num > 0:
  num = int(input("Inserisci un numero: "))
  if num == 0:
    break
  somma = somma + num

print("La somma dei numeri è di ", somma )