# Write code below 💖
#This code creates a Pokedex of Pokemon using classes, init method, and instance methods.

class Pokemon:
  def __init__(self, entry, name, types, description, is_caught, classification, abilities):
    self.entry = entry
    self.name = name
    self.types = types
    self.description = description
    self.is_caught = is_caught
    self.classification = classification
    self.abilities = abilities

  def speak(self):
    print("This Pokemon's cry sounds like " + self.name + ", " + self.name + "!")

  def display_details(self):
    print("Here are the details of your selected Pokemon ")
    print("Entry: ", self.entry)
    print("Name: ", self.name)
    print("Types: ", self.types)
    print("Description: ", self.description)
    print("Is Caught: ", self.is_caught)
    print("Classification: ", self.classification)
    print("Abilities: ", self.abilities)

polywrath = Pokemon(62, "Polywrath", ["water", "fighting"], "It can use its well developed arms and legs to run on the surface of the water for a split second.", True, "Tadpole Pokemon", ["water absorb", "damp"])

anorith = Pokemon(347, "Anorith", ["rock", "bug"], "This Pokemon ancestor was reanimated from a fossil. It lived in the sea, and hunted with it\s claws.", False, "Old Shrimp Pokemon", ["battle armor"])

flabebe = Pokemon(669, "Flabebe", ["fairy"], "It receives strength from flowerd and gives them someif it\s energy in return. This pokemon likes orange flowers bext of all.", True, "Single Bloom Pokemon", ["flower veil"])

polywrath.speak()
polywrath.display_details()

anorith.speak()
anorith.display_details()

flabebe.speak()
anorith.display_details()