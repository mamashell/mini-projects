# Write code below 💖
# This code calculates the area of a random planet using imported functions from the math and random modules

from math import pi
from random import choice as ch
from math import ceil

planets = [
  'Mercury',
  'Venus',
  'Earth',
  'Mars',
  'Saturn'
]

random_planet = ch(planets)
r = 0

if random_planet == 'Mercury':
  r = 2440
elif random_planet == 'Venus':
  r = 6052
elif random_planet == 'Earth':
  r = 6371
elif random_planet == 'Mars':
  r = 3390
elif random_planet == 'Saturn':
  r = 58232
else:
    print('Oops! An error occurred.')

def area(random_planet):
  area = ceil(4 * pi * r * r)
  return area

print(f'Random Planet: {random_planet}')
print(f'The Area of this planet is {area(random_planet)}')

