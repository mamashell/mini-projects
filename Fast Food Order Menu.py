# Write code below 💖
# This function allows you to order from Taco Bell's Cravings Value Menu. Yummm, Late Night snacks!

cravings_menu = [
  "Cheesy Roll Up",
  "Spicy Potato Soft Taco",
  "Cheesy Bean and Rice Burrito",
  "Double Stacked Taco",
  "Stacker",
  "3 Cheese Chicken Flatbread Melt",
  "Cheesy Fiesta Potates",
  "Chicken Enchilada Burrito",
  "Cheesy Double Beef Burrito",
  "Loaded Beef Nachos"
]

def get_item(x):
  if x == 1:
    print(cravings_menu[0])
  elif x == 2:
    print(cravings_menu[1])
  elif x == 3:
    print(cravings_menu[2])
  elif x == 4:
    print(cravings_menu[3])
  elif x == 5:
    print(cravings_menu[4])
  elif x == 6:
    print(cravings_menu[5])
  elif x == 7:
    print(cravings_menu[6])
  elif x == 8:
    print(cravings_menu[7])
  elif x == 9:
    print(cravings_menu[8])
  elif x == 10:
    print(cravings_menu[9])
  elif x == 11:
    print(cravings_menu[10])
  else:
    print("Invalid Input")    

def welcome():
  print("Hello! Thank you for visiting Taco Bell. Our Late Night Cravings Value Menu is out of this world. Please see your choices below: ")
  print("1. Cheesy Roll Up")
  print("2. Spicy Potato Soft Taco")
  print("3. Cheesy Bean and Rice Burrito")
  print("4. Double Stacked Taco")
  print("5. Stacker")
  print("6. 3 Cheese Chicken Flatbread Melt")
  print("7. Cheesy Fiesta Potatoes")
  print("8. Chicken Enchilada Burrito")
  print("9. Cheesy Double Beef Burrito")
  print("10. Loaded Beef Nachos")

welcome()

option = int(input("What would you like to order? "))
get_item(option)