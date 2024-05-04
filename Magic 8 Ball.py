# Write code below 💖

#Use this to have a Magic 8 Ball answer any yes or no question
import random

question = input('Question:     ')

random_number = random.randint(1, 9)

if random_number == 1:
  print("Magic 8 Ball says: Yes - definitely.")
elif random_number == 2:
  print("Magic 8 Ball says: It is decidedly so.")
elif random_number == 3:
  print("Magic 8 Ball says: Without a doubt.")
elif random_number == 4:
  print("Magic 8 Ball says: Reply hazy, try again.")
elif random_number == 5:
  print("Magic 8 Ball says: Ask again later.")
elif random_number == 6:
  print("Magic 8 Ball says: Better not tell you now.")
elif random_number == 7:
  print("Magic 8 Ball says: My sources say no.")
elif random_number == 8:
  print("Magic 8 Ball Says: Outlook not so good.")
elif random_number == 9:
  print("Magic 8 Ball Says: Very doubtful.")
else:
  print("Try Again.")
