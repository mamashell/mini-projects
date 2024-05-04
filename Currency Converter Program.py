# Write code below 💖

# This code converts multiple currencies to USD

pesos = .00026
soles = .26
reais = .20


currency_pesos = int(input("What do you have left in pesos? "))
print(currency_pesos)

currency_soles = int(input("What do you have left in soles? "))
print(currency_soles)

currency_reais = int(input("What do you have left in reais? "))
print(currency_reais)

total = (pesos * currency_pesos) + (soles * currency_soles) + (reais * currency_reais)
print(total)