# Write code below 💖
# This uses the random module to create a slot machine! This is the simple version

import random

symbols = [ '🍒', '🍇', '🍉', '7️⃣']

results = random.choices(symbols, k=3)

print(f'{results[0]} | {results[1]} | {results[2]}')

if (results[0] == '7️⃣' and results[1] == '7️⃣' and results[2] == '7️⃣'):
  print("Jackpot! 💰")
else:
  print("Thanks for playing!")