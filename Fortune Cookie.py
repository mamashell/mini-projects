# Write code below 💖
#This program provides a random fortune cookie using lists and the def function

import random

cookies = [
    "Don't pursue happiness – create it.", 
    "All things are difficult before they are easy.", 
    "The early bird gets the worm, but the second mouse gets the cheese.", 
    "Someone in your life needs a letter from you.", 
    "Don't just think. Act!", 
    "Your heart will skip a beat.", 
    "The fortune you search for is in another cookie.", 
    "Help! I'm being held prisoner in a Chinese bakery!"
    ]

def fortune():
  random_number = random.randint(0,7)
  if random_number == 0:
    print(cookies[0])
  elif random_number == 1:
    print(cookies[1])
  elif random_number == 2:
    print(cookies[2])
  elif random_number == 3:
    print(cookies[3])
  elif random_number == 4:
    print(cookies[4])
  elif random_number == 5:
    print(cookies[5])
  elif random_number == 6:
    print(cookies[6])
  elif random_number == 7:
    print(cookies[7])
  else:
    print("Try Again.")    
  return random_number

fortune()
fortune()
fortune()