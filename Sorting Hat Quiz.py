# Write code below 💖

#This is a Harry Potter Sorting Hat quiz!
Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

question_one = int(input("""Q1) Do you like Dawn or Dusk? 
1) Dawn 
2) Dusk\n"""))

if question_one == 1:
  Gryffindor += 1
  Ravenclaw += 1
elif question_one == 2:
  Hufflepuff += 1
  Slytherin += 1
else:
  print("Wrong input.")

question_two = int(input("""Q2) When I'm dead, I want people to remember me as: 
1) The Good 
2) The Great
3) The Wise
4) The Bold\n"""))

if question_two == 1:
  Hufflepuff += 2
elif question_two == 2:
  Slytherin += 2
elif question_two == 3:
  Ravenclaw += 2
elif question_two == 4:
  Gryffindor + 2
else:
  print("Wrong input.")

question_three = int(input("""Q3) Which kind of instrument most pleases your ear? 
1) The violin 
2) The trumpet
3) The piano
4) The drum\n"""))

if question_three == 1:
  Slytherin += 4
elif question_three == 2:
  Hufflepuff += 4
elif question_three == 3:
  Ravenclaw += 4
elif question_three == 4:
  Gryffindor += 4
else:
  print("Wrong input.")

#This is a dictionary of all the house points user received
house_points = {
  'Gryffindor': Gryffindor,
  'Ravenclaw': Ravenclaw,
  'Hufflepuff': Hufflepuff,
  'Slytherin': Slytherin
}

#This is used to find the maximum number of house points
max_house = max(house_points, key=house_points.get)

print("Gryffindor Points: ", Gryffindor)
print("Ravenclaw Points: ", Ravenclaw)
print("Hufflepuff Points: ", Hufflepuff)
print("Slytherin Points: ", Slytherin)    

print(f"Sorting Hat says: I know just what to do with you...your house is {max_house}!!")