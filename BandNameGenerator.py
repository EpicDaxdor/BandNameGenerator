import random

# Define lists of words

adjectives = [
    'Flying', 'Red', 'Silent', 'Broken', 'Dark', 'Mysterious',
    'Wild', 'Happy', 'Electric', 'Golden', 'Ancient', 'Loud'
]

nouns = [
    'Dragons', 'Wolves', 'Pirates', 'Stars', 'Echoes', 'Storms',
    'Mirrors', 'Voices', 'Giants', 'Rangers', 'Warriors', 'Knights'
]

# Define a function to generate a band name

def generate_band_name():
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    return f"{adjective} {noun}"

# generate multiple band names
for _ in range(10):
  print(generate_band_name())
