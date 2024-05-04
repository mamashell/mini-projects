# Write code below 💖
# This code shows information about my hometown and favorite cities using the init method

class City():
  def __init__(self, name, country, population, landmarks, nickname, food):
    self.name = name
    self.country = country
    self.population = population
    self.landmarks = landmarks
    self.nickname = nickname
    self.food = food

tampa = City("Tampa", "United States", 387000, ["Tampa Bay", "Raymond James Staduium", "Dali Museum", "TB Convention Center"], "The Bay", "Cuban Sandwich")
seattle = City("Seattle", "United States", 734000, ["Space Needle", "Seattle Public Library", "Seattle Center", "Seattle Waterfront"], "Emerald City", "Dutch Baby")

print(vars(tampa))
print(vars(seattle))